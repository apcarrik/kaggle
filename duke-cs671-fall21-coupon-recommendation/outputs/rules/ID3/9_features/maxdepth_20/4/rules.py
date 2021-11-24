def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 8148, "metric_value": 0.9876, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 5867, "metric_value": 0.9568, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Distance", "instances": 3640, "metric_value": 0.982, "depth": 3}
			if obj[8]<=1:
				# {"feature": "Time", "instances": 1967, "metric_value": 0.9259, "depth": 4}
				if obj[1]>0:
					# {"feature": "Direction_same", "instances": 1275, "metric_value": 0.9001, "depth": 5}
					if obj[7]>0:
						# {"feature": "Occupation", "instances": 658, "metric_value": 0.9501, "depth": 6}
						if obj[4]<=18.69112571963794:
							# {"feature": "Bar", "instances": 606, "metric_value": 0.9589, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Education", "instances": 419, "metric_value": 0.943, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Restaurant20to50", "instances": 380, "metric_value": 0.9515, "depth": 9}
									if obj[6]<=3.0:
										return 'True'
									elif obj[6]>3.0:
										return 'True'
									else: return 'True'
								elif obj[3]>3:
									# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.8213, "depth": 9}
									if obj[6]<=2.0:
										return 'True'
									elif obj[6]>2.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								# {"feature": "Restaurant20to50", "instances": 187, "metric_value": 0.9849, "depth": 8}
								if obj[6]>-1.0:
									# {"feature": "Education", "instances": 185, "metric_value": 0.9868, "depth": 9}
									if obj[3]>1:
										return 'True'
									elif obj[3]<=1:
										return 'True'
									else: return 'True'
								elif obj[6]<=-1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>18.69112571963794:
							# {"feature": "Education", "instances": 52, "metric_value": 0.7793, "depth": 7}
							if obj[3]>1:
								# {"feature": "Bar", "instances": 28, "metric_value": 0.9059, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9641, "depth": 9}
									if obj[6]<=1.0:
										return 'True'
									elif obj[6]>1.0:
										return 'False'
									else: return 'False'
								elif obj[5]>1.0:
									# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[6]<=2.0:
										return 'True'
									elif obj[6]>2.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=1:
								# {"feature": "Bar", "instances": 24, "metric_value": 0.5436, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.7496, "depth": 9}
									if obj[6]<=1.0:
										return 'True'
									else: return 'True'
								elif obj[5]>0.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]<=0:
						# {"feature": "Education", "instances": 617, "metric_value": 0.8257, "depth": 6}
						if obj[3]<=4:
							# {"feature": "Bar", "instances": 612, "metric_value": 0.8289, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Occupation", "instances": 397, "metric_value": 0.7939, "depth": 8}
								if obj[4]<=13.127150746831763:
									# {"feature": "Restaurant20to50", "instances": 342, "metric_value": 0.7642, "depth": 9}
									if obj[6]<=2.0:
										return 'True'
									elif obj[6]>2.0:
										return 'True'
									else: return 'True'
								elif obj[4]>13.127150746831763:
									# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.9299, "depth": 9}
									if obj[6]>0.0:
										return 'True'
									elif obj[6]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[5]>1.0:
								# {"feature": "Restaurant20to50", "instances": 215, "metric_value": 0.8841, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Occupation", "instances": 195, "metric_value": 0.8512, "depth": 9}
									if obj[4]<=19.57855234816141:
										return 'True'
									elif obj[4]>19.57855234816141:
										return 'True'
									else: return 'True'
								elif obj[6]<=0.0:
									# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 9}
									if obj[4]<=8:
										return 'True'
									elif obj[4]>8:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[3]>4:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Restaurant20to50", "instances": 692, "metric_value": 0.963, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Bar", "instances": 554, "metric_value": 0.9465, "depth": 6}
						if obj[5]<=3.0:
							# {"feature": "Education", "instances": 540, "metric_value": 0.9405, "depth": 7}
							if obj[3]<=4:
								# {"feature": "Direction_same", "instances": 535, "metric_value": 0.9433, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Occupation", "instances": 333, "metric_value": 0.9569, "depth": 9}
									if obj[4]<=13.93858607217959:
										return 'True'
									elif obj[4]>13.93858607217959:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									# {"feature": "Occupation", "instances": 202, "metric_value": 0.9166, "depth": 9}
									if obj[4]>1.884015305169564:
										return 'True'
									elif obj[4]<=1.884015305169564:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>4:
								return 'True'
							else: return 'True'
						elif obj[5]>3.0:
							# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 7}
							if obj[4]<=7:
								# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[3]>2:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]<=2:
									return 'True'
								else: return 'True'
							elif obj[4]>7:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]<=0.0:
						# {"feature": "Occupation", "instances": 138, "metric_value": 0.9986, "depth": 6}
						if obj[4]<=16:
							# {"feature": "Education", "instances": 128, "metric_value": 1.0, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Bar", "instances": 113, "metric_value": 0.9986, "depth": 8}
								if obj[5]>-1.0:
									# {"feature": "Direction_same", "instances": 112, "metric_value": 0.9979, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[5]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[3]>3:
								# {"feature": "Bar", "instances": 15, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Direction_same", "instances": 14, "metric_value": 0.8631, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[5]>1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]>16:
							# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[5]>0.0:
								return 'True'
							elif obj[5]<=0.0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]>0:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=3:
										return 'True'
									else: return 'True'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[8]>1:
				# {"feature": "Time", "instances": 1673, "metric_value": 0.9993, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Direction_same", "instances": 1401, "metric_value": 0.9951, "depth": 5}
					if obj[7]<=0:
						# {"feature": "Education", "instances": 1064, "metric_value": 0.9815, "depth": 6}
						if obj[3]>0:
							# {"feature": "Bar", "instances": 713, "metric_value": 0.9674, "depth": 7}
							if obj[5]>-1.0:
								# {"feature": "Restaurant20to50", "instances": 708, "metric_value": 0.9691, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Occupation", "instances": 452, "metric_value": 0.9806, "depth": 9}
									if obj[4]<=13.593750861224173:
										return 'False'
									elif obj[4]>13.593750861224173:
										return 'True'
									else: return 'True'
								elif obj[6]>1.0:
									# {"feature": "Occupation", "instances": 256, "metric_value": 0.9422, "depth": 9}
									if obj[4]<=14:
										return 'False'
									elif obj[4]>14:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[3]<=0:
							# {"feature": "Restaurant20to50", "instances": 351, "metric_value": 0.9979, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Occupation", "instances": 331, "metric_value": 0.9945, "depth": 8}
								if obj[4]<=19.162870032175782:
									# {"feature": "Bar", "instances": 311, "metric_value": 0.9961, "depth": 9}
									if obj[5]>0.0:
										return 'False'
									elif obj[5]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[4]>19.162870032175782:
									# {"feature": "Bar", "instances": 20, "metric_value": 0.9341, "depth": 9}
									if obj[5]<=2.0:
										return 'False'
									elif obj[5]>2.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>2.0:
								# {"feature": "Occupation", "instances": 20, "metric_value": 0.8113, "depth": 8}
								if obj[4]>1:
									# {"feature": "Bar", "instances": 15, "metric_value": 0.9183, "depth": 9}
									if obj[5]<=2.0:
										return 'True'
									elif obj[5]>2.0:
										return 'False'
									else: return 'False'
								elif obj[4]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]>0:
						# {"feature": "Restaurant20to50", "instances": 337, "metric_value": 0.9807, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Occupation", "instances": 241, "metric_value": 0.9955, "depth": 7}
							if obj[4]>0:
								# {"feature": "Bar", "instances": 238, "metric_value": 0.9967, "depth": 8}
								if obj[5]>0.0:
									# {"feature": "Education", "instances": 133, "metric_value": 1.0, "depth": 9}
									if obj[3]<=2:
										return 'True'
									elif obj[3]>2:
										return 'False'
									else: return 'False'
								elif obj[5]<=0.0:
									# {"feature": "Education", "instances": 105, "metric_value": 0.981, "depth": 9}
									if obj[3]<=1:
										return 'True'
									elif obj[3]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>1.0:
							# {"feature": "Bar", "instances": 96, "metric_value": 0.896, "depth": 7}
							if obj[5]<=3.0:
								# {"feature": "Occupation", "instances": 94, "metric_value": 0.8787, "depth": 8}
								if obj[4]>3:
									# {"feature": "Education", "instances": 68, "metric_value": 0.8113, "depth": 9}
									if obj[3]>1:
										return 'True'
									elif obj[3]<=1:
										return 'True'
									else: return 'True'
								elif obj[4]<=3:
									# {"feature": "Education", "instances": 26, "metric_value": 0.9829, "depth": 9}
									if obj[3]<=2:
										return 'True'
									elif obj[3]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>3.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[1]>3:
					# {"feature": "Bar", "instances": 272, "metric_value": 0.9597, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Occupation", "instances": 194, "metric_value": 0.939, "depth": 6}
						if obj[4]>1.7184539250860258:
							# {"feature": "Education", "instances": 162, "metric_value": 0.912, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Restaurant20to50", "instances": 149, "metric_value": 0.927, "depth": 8}
								if obj[6]>-1.0:
									# {"feature": "Direction_same", "instances": 147, "metric_value": 0.9249, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=-1.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>3:
								# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.6194, "depth": 8}
								if obj[6]<=1.0:
									return 'True'
								elif obj[6]>1.0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]<=1.7184539250860258:
							# {"feature": "Education", "instances": 32, "metric_value": 1.0, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.9992, "depth": 8}
								if obj[6]>-1.0:
									# {"feature": "Direction_same", "instances": 30, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[3]>3:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]>1.0:
						# {"feature": "Occupation", "instances": 78, "metric_value": 0.9924, "depth": 6}
						if obj[4]<=12:
							# {"feature": "Education", "instances": 57, "metric_value": 0.9998, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Restaurant20to50", "instances": 44, "metric_value": 0.994, "depth": 8}
								if obj[6]<=3.0:
									# {"feature": "Direction_same", "instances": 43, "metric_value": 0.9965, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]>3.0:
									return 'True'
								else: return 'True'
							elif obj[3]>2:
								# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[6]>2.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>12:
							# {"feature": "Education", "instances": 21, "metric_value": 0.8631, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Direction_same", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[3]>2:
								# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[6]<=2.0:
									return 'True'
								elif obj[6]>2.0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Bar", "instances": 2227, "metric_value": 0.8909, "depth": 3}
			if obj[5]<=3.0:
				# {"feature": "Education", "instances": 2155, "metric_value": 0.8855, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Restaurant20to50", "instances": 2017, "metric_value": 0.8919, "depth": 5}
					if obj[6]<=1.0:
						# {"feature": "Occupation", "instances": 1346, "metric_value": 0.9102, "depth": 6}
						if obj[4]<=18.987721595523922:
							# {"feature": "Distance", "instances": 1226, "metric_value": 0.9186, "depth": 7}
							if obj[8]>1:
								# {"feature": "Time", "instances": 810, "metric_value": 0.9081, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 579, "metric_value": 0.8861, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Direction_same", "instances": 231, "metric_value": 0.9524, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]<=1:
								# {"feature": "Time", "instances": 416, "metric_value": 0.937, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Direction_same", "instances": 266, "metric_value": 0.9701, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									# {"feature": "Direction_same", "instances": 150, "metric_value": 0.8462, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>18.987721595523922:
							# {"feature": "Time", "instances": 120, "metric_value": 0.7978, "depth": 7}
							if obj[1]>0:
								# {"feature": "Distance", "instances": 94, "metric_value": 0.8196, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 64, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 30, "metric_value": 0.8366, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Distance", "instances": 26, "metric_value": 0.7063, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 18, "metric_value": 0.65, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>1.0:
						# {"feature": "Occupation", "instances": 671, "metric_value": 0.8495, "depth": 6}
						if obj[4]>2.6698839925737703:
							# {"feature": "Distance", "instances": 552, "metric_value": 0.8732, "depth": 7}
							if obj[8]>1:
								# {"feature": "Time", "instances": 371, "metric_value": 0.8447, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 296, "metric_value": 0.878, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 75, "metric_value": 0.6653, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]<=1:
								# {"feature": "Time", "instances": 181, "metric_value": 0.9219, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 130, "metric_value": 0.9558, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Direction_same", "instances": 51, "metric_value": 0.7871, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]<=2.6698839925737703:
							# {"feature": "Time", "instances": 119, "metric_value": 0.7083, "depth": 7}
							if obj[1]>0:
								# {"feature": "Distance", "instances": 92, "metric_value": 0.7936, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 61, "metric_value": 0.8537, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 31, "metric_value": 0.6374, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Distance", "instances": 27, "metric_value": 0.2285, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 19, "metric_value": 0.2975, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>3:
					# {"feature": "Occupation", "instances": 138, "metric_value": 0.7685, "depth": 5}
					if obj[4]<=12:
						# {"feature": "Restaurant20to50", "instances": 109, "metric_value": 0.8357, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Time", "instances": 84, "metric_value": 0.7919, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Distance", "instances": 54, "metric_value": 0.7642, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 30, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 24, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Distance", "instances": 30, "metric_value": 0.8366, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 18, "metric_value": 0.8524, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>1.0:
							# {"feature": "Time", "instances": 25, "metric_value": 0.9427, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[4]>12:
						# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.3621, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Time", "instances": 17, "metric_value": 0.5226, "depth": 7}
							if obj[1]>0:
								# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[5]>3.0:
				# {"feature": "Occupation", "instances": 72, "metric_value": 0.9911, "depth": 4}
				if obj[4]<=12:
					# {"feature": "Education", "instances": 51, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.9612, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Distance", "instances": 37, "metric_value": 0.974, "depth": 7}
							if obj[8]>1:
								# {"feature": "Time", "instances": 21, "metric_value": 0.9183, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 17, "metric_value": 0.9367, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]<=1:
								# {"feature": "Time", "instances": 16, "metric_value": 1.0, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9957, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Distance", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[8]>1:
							# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[1]>0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[6]>1.0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=1.0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[8]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>12:
					# {"feature": "Time", "instances": 21, "metric_value": 0.8631, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[6]>1.0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=1.0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'True'
									elif obj[8]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>0:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[8]>1:
								return 'False'
							elif obj[8]<=1:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]>2.0:
									return 'False'
								elif obj[6]<=2.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2281, "metric_value": 0.9817, "depth": 2}
		if obj[5]>0.0:
			# {"feature": "Restaurant20to50", "instances": 1323, "metric_value": 0.9981, "depth": 3}
			if obj[6]<=1.0:
				# {"feature": "Education", "instances": 799, "metric_value": 0.9977, "depth": 4}
				if obj[3]>0:
					# {"feature": "Occupation", "instances": 523, "metric_value": 0.9851, "depth": 5}
					if obj[4]<=19.589348592298702:
						# {"feature": "Passanger", "instances": 498, "metric_value": 0.9902, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Time", "instances": 432, "metric_value": 0.981, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Distance", "instances": 286, "metric_value": 0.9987, "depth": 8}
								if obj[8]<=2:
									# {"feature": "Direction_same", "instances": 209, "metric_value": 0.9972, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[8]>2:
									# {"feature": "Direction_same", "instances": 77, "metric_value": 0.9999, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Direction_same", "instances": 146, "metric_value": 0.883, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 131, "metric_value": 0.8588, "depth": 9}
									if obj[8]<=2:
										return 'False'
									elif obj[8]>2:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									# {"feature": "Distance", "instances": 15, "metric_value": 0.9968, "depth": 9}
									if obj[8]<=2:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>2:
							# {"feature": "Time", "instances": 66, "metric_value": 0.976, "depth": 7}
							if obj[1]>2:
								# {"feature": "Distance", "instances": 53, "metric_value": 0.9562, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 44, "metric_value": 0.9457, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=2:
								# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9957, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 9}
									if obj[8]<=2:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>19.589348592298702:
						# {"feature": "Distance", "instances": 25, "metric_value": 0.6343, "depth": 6}
						if obj[8]<=2:
							# {"feature": "Time", "instances": 19, "metric_value": 0.7425, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Passanger", "instances": 15, "metric_value": 0.8366, "depth": 8}
								if obj[0]>0:
									# {"feature": "Direction_same", "instances": 11, "metric_value": 0.684, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[0]<=0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]>3:
								return 'False'
							else: return 'False'
						elif obj[8]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]<=0:
					# {"feature": "Occupation", "instances": 276, "metric_value": 0.9915, "depth": 5}
					if obj[4]<=21:
						# {"feature": "Time", "instances": 266, "metric_value": 0.9951, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Passanger", "instances": 172, "metric_value": 0.9749, "depth": 7}
							if obj[0]>0:
								# {"feature": "Direction_same", "instances": 154, "metric_value": 0.9852, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 101, "metric_value": 0.9943, "depth": 9}
									if obj[8]>1:
										return 'True'
									elif obj[8]<=1:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									# {"feature": "Distance", "instances": 53, "metric_value": 0.9562, "depth": 9}
									if obj[8]<=1:
										return 'True'
									elif obj[8]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[0]<=0:
								# {"feature": "Distance", "instances": 18, "metric_value": 0.7642, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Passanger", "instances": 94, "metric_value": 0.9918, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Distance", "instances": 58, "metric_value": 0.9124, "depth": 8}
								if obj[8]<=2:
									# {"feature": "Direction_same", "instances": 57, "metric_value": 0.8997, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[8]>2:
									return 'True'
								else: return 'True'
							elif obj[0]>2:
								# {"feature": "Distance", "instances": 36, "metric_value": 0.9436, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 27, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>21:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[8]>1:
							return 'True'
						elif obj[8]<=1:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[6]>1.0:
				# {"feature": "Time", "instances": 524, "metric_value": 0.9668, "depth": 4}
				if obj[1]>0:
					# {"feature": "Passanger", "instances": 385, "metric_value": 0.9852, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Occupation", "instances": 316, "metric_value": 0.9951, "depth": 6}
						if obj[4]>0:
							# {"feature": "Education", "instances": 313, "metric_value": 0.9961, "depth": 7}
							if obj[3]>1:
								# {"feature": "Distance", "instances": 201, "metric_value": 0.9998, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 126, "metric_value": 0.9993, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 75, "metric_value": 0.9937, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[3]<=1:
								# {"feature": "Distance", "instances": 112, "metric_value": 0.9769, "depth": 8}
								if obj[8]<=2:
									# {"feature": "Direction_same", "instances": 88, "metric_value": 0.9865, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[8]>2:
									# {"feature": "Direction_same", "instances": 24, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						# {"feature": "Education", "instances": 69, "metric_value": 0.8685, "depth": 6}
						if obj[3]>1:
							# {"feature": "Occupation", "instances": 46, "metric_value": 0.9503, "depth": 7}
							if obj[4]>3:
								# {"feature": "Distance", "instances": 35, "metric_value": 0.9852, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 30, "metric_value": 0.9968, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=3:
								# {"feature": "Distance", "instances": 11, "metric_value": 0.684, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=1:
							# {"feature": "Occupation", "instances": 23, "metric_value": 0.5586, "depth": 7}
							if obj[4]<=5:
								# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							elif obj[4]>5:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 139, "metric_value": 0.875, "depth": 5}
					if obj[8]>1:
						# {"feature": "Passanger", "instances": 76, "metric_value": 0.9754, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Occupation", "instances": 68, "metric_value": 0.9488, "depth": 7}
							if obj[4]>0:
								# {"feature": "Education", "instances": 66, "metric_value": 0.9572, "depth": 8}
								if obj[3]>0:
									# {"feature": "Direction_same", "instances": 45, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9984, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[4]>7:
								# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[3]>1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]<=1:
									return 'True'
								else: return 'True'
							elif obj[4]<=7:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[8]<=1:
						# {"feature": "Passanger", "instances": 63, "metric_value": 0.6313, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 60, "metric_value": 0.5665, "depth": 7}
							if obj[3]<=4:
								# {"feature": "Occupation", "instances": 58, "metric_value": 0.5313, "depth": 8}
								if obj[4]<=9.689655172413794:
									# {"feature": "Direction_same", "instances": 31, "metric_value": 0.6374, "depth": 9}
									if obj[7]<=1:
										return 'True'
									else: return 'True'
								elif obj[4]>9.689655172413794:
									# {"feature": "Direction_same", "instances": 27, "metric_value": 0.3809, "depth": 9}
									if obj[7]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>4:
								# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>1:
									return 'False'
								elif obj[4]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[5]<=0.0:
			# {"feature": "Restaurant20to50", "instances": 958, "metric_value": 0.8493, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Distance", "instances": 916, "metric_value": 0.833, "depth": 4}
				if obj[8]<=2:
					# {"feature": "Education", "instances": 733, "metric_value": 0.8641, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Occupation", "instances": 672, "metric_value": 0.8469, "depth": 6}
						if obj[4]>1.2431468770663034:
							# {"feature": "Time", "instances": 526, "metric_value": 0.8723, "depth": 7}
							if obj[1]>0:
								# {"feature": "Direction_same", "instances": 351, "metric_value": 0.8383, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Passanger", "instances": 308, "metric_value": 0.8544, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									# {"feature": "Passanger", "instances": 43, "metric_value": 0.6931, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]<=0:
								# {"feature": "Direction_same", "instances": 175, "metric_value": 0.9275, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Passanger", "instances": 94, "metric_value": 0.9601, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									# {"feature": "Passanger", "instances": 81, "metric_value": 0.8767, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[4]<=1.2431468770663034:
							# {"feature": "Passanger", "instances": 146, "metric_value": 0.7328, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Time", "instances": 85, "metric_value": 0.6723, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 52, "metric_value": 0.57, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 33, "metric_value": 0.799, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Direction_same", "instances": 61, "metric_value": 0.8047, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Time", "instances": 57, "metric_value": 0.7425, "depth": 9}
									if obj[1]>2:
										return 'False'
									elif obj[1]<=2:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[1]<=3:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[3]>3:
						# {"feature": "Occupation", "instances": 61, "metric_value": 0.9842, "depth": 6}
						if obj[4]<=11:
							# {"feature": "Time", "instances": 55, "metric_value": 0.9457, "depth": 7}
							if obj[1]>1:
								# {"feature": "Passanger", "instances": 28, "metric_value": 0.8631, "depth": 8}
								if obj[0]>0:
									# {"feature": "Direction_same", "instances": 20, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[0]<=0:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=1:
								# {"feature": "Passanger", "instances": 27, "metric_value": 0.9911, "depth": 8}
								if obj[0]>0:
									# {"feature": "Direction_same", "instances": 24, "metric_value": 0.995, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]<=0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>11:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[8]>2:
					# {"feature": "Passanger", "instances": 183, "metric_value": 0.6687, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Occupation", "instances": 179, "metric_value": 0.6257, "depth": 6}
						if obj[4]>0:
							# {"feature": "Education", "instances": 175, "metric_value": 0.5917, "depth": 7}
							if obj[3]<=4:
								# {"feature": "Time", "instances": 174, "metric_value": 0.5788, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Direction_same", "instances": 164, "metric_value": 0.6006, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							elif obj[3]>4:
								return 'True'
							else: return 'True'
						elif obj[4]<=0:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>2.0:
				# {"feature": "Education", "instances": 42, "metric_value": 0.9984, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Occupation", "instances": 21, "metric_value": 0.7919, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Passanger", "instances": 13, "metric_value": 0.9612, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]>1:
										return 'False'
									elif obj[8]<=1:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[4]>4:
						return 'True'
					else: return 'True'
				elif obj[3]>0:
					# {"feature": "Time", "instances": 21, "metric_value": 0.8631, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 6}
						if obj[4]>5:
							# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 7}
							if obj[0]>1:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[7]<=0:
									return 'False'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							elif obj[0]<=1:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]>1:
										return 'False'
									elif obj[8]<=1:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]<=5:
							# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[8]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'False'
