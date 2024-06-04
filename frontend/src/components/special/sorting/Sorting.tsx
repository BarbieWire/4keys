import React, { useRef, Dispatch, SetStateAction } from 'react';
import { useAppDispatch, useAppSelector } from '../../../redux/hooks';
import { updateDraggableStrip } from '../../../redux/slices/appearanceSlice';
import classes from './Sorting.module.css'
import { showPerClick } from '../constants';

import { v4 as uuidv4 } from 'uuid';


interface ComponentProps {
    sortingCategories: string[],
    highlightedCategory: string,
    setHighlightedCategory: Dispatch<SetStateAction<string>>,
    setDisplayAmount: Dispatch<SetStateAction<number>>,
}

const Sorting: React.FC<ComponentProps> = (props) => {
    const { sortingCategories, highlightedCategory, setHighlightedCategory, setDisplayAmount } = props

    const dispatch = useAppDispatch()
    const stripState = useAppSelector(state => state.websiteAppearance.draggableStrip)

    const ref = useRef<HTMLDivElement>(null!) // ref to div w/ class: .item_wrapper

    // onscroll
    function ScrollWheel(e: React.WheelEvent) {
        const elem = ref.current
        elem.scrollTo({
            left: elem.scrollLeft + e.deltaY * 3,
            behavior: "smooth"
        })
    }

    // drag stop
    function DragPrevent() {
        const timer = setTimeout(() => {
            dispatch(updateDraggableStrip({
                dragging: false,
                moving: false
            }))
        }, 10)
        return () => clearTimeout(timer)
    }

    const MouseUp = () => {
        DragPrevent()
    }

    const onMouseDown = (e: React.MouseEvent) => {
        e.preventDefault()
        dispatch(updateDraggableStrip({
            dragging: true,
            startX: e.pageX - ref.current.offsetLeft,
            scrollLeft: ref.current.scrollLeft
        }))
    }

    // start dragging
    const onMouseMove = (e: React.MouseEvent) => {
        e.preventDefault()
        const { dragging, startX, scrollLeft } = stripState
        if (dragging) {
            dispatch(updateDraggableStrip({
                moving: true
            }))

            const movingTo = e.pageX - ref.current.offsetLeft
            const move = movingTo - startX
            ref.current.scrollLeft = scrollLeft - move
        }
    }

    const onMouseLeave = () => {
        dispatch(updateDraggableStrip({
            dragging: false,
            moving: false
        }))
    }

    function highlightCategory(name: string) {
        setDisplayAmount(showPerClick)
        if (stripState.moving) {
            return
        }
        setHighlightedCategory(name)
    }

    return (
        <div
            className={classes.sorting_wrapper}
            onMouseUp={MouseUp}
            onMouseDown={onMouseDown}
            onMouseMove={onMouseMove}
            onMouseLeave={onMouseLeave}
        >
            <div
                className={classes.item_wrapper}
                ref={ref}
                onWheel={ScrollWheel}
            >
                {
                    sortingCategories.map((category, index) => {
                        return <div
                            id={uuidv4()}
                            onClick={() => highlightCategory(category)}
                            className={
                                category === highlightedCategory
                                    ? [classes.category_selector, classes.active].join(" ")
                                    : classes.category_selector
                            }
                        >
                            <span className={classes.text_nowrap}>{category}</span>
                        </div>
                    })
                }
            </div>
        </div>
    );
};

export default Sorting;