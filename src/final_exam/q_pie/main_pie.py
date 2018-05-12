from src.final_exam.q_pie.pie_arc import PieArc
from src.final_exam.q_pie.pie_chart import PieChart

arcs = [PieArc('one'), PieArc('two'), PieArc('three'), PieArc('four')]

pie = PieChart(arcs)

pie.draw()
