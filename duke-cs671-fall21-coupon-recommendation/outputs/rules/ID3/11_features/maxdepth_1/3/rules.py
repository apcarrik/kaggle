def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4716, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5887, "metric_value": 0.4562, "depth": 2}
		if obj[7]<=1.0:
			# {"feature": "Distance", "instances": 3057, "metric_value": 0.4852, "depth": 3}
			if obj[10]<=2:
				# {"feature": "Passanger", "instances": 2765, "metric_value": 0.4824, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 1675, "metric_value": 0.4929, "depth": 5}
					if obj[8]<=2.0:
						# {"feature": "Time", "instances": 1620, "metric_value": 0.4957, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Direction_same", "instances": 998, "metric_value": 0.4947, "depth": 7}
							if obj[9]>0:
								# {"feature": "Occupation", "instances": 544, "metric_value": 0.4879, "depth": 8}
								if obj[5]<=7.757352941176471:
									# {"feature": "Bar", "instances": 348, "metric_value": 0.4933, "depth": 9}
									if obj[6]>-1.0:
										# {"feature": "Age", "instances": 342, "metric_value": 0.4953, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 277, "metric_value": 0.4984, "depth": 11}
											if obj[4]<=2:
												return 'True'
											elif obj[4]>2:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Education", "instances": 65, "metric_value": 0.4722, "depth": 11}
											if obj[4]<=2:
												return 'True'
											elif obj[4]>2:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[6]<=-1.0:
										# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[4]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]>7.757352941176471:
									# {"feature": "Education", "instances": 196, "metric_value": 0.4621, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Age", "instances": 149, "metric_value": 0.4384, "depth": 10}
										if obj[3]<=3:
											# {"feature": "Bar", "instances": 95, "metric_value": 0.4031, "depth": 11}
											if obj[6]<=1.0:
												return 'True'
											elif obj[6]>1.0:
												return 'True'
											else: return 'True'
										elif obj[3]>3:
											# {"feature": "Bar", "instances": 54, "metric_value": 0.4786, "depth": 11}
											if obj[6]<=2.0:
												return 'True'
											elif obj[6]>2.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>2:
										# {"feature": "Bar", "instances": 47, "metric_value": 0.4642, "depth": 10}
										if obj[6]<=1.0:
											# {"feature": "Age", "instances": 44, "metric_value": 0.4893, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[6]>1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[9]<=0:
								# {"feature": "Age", "instances": 454, "metric_value": 0.4951, "depth": 8}
								if obj[3]<=6:
									# {"feature": "Education", "instances": 428, "metric_value": 0.4979, "depth": 9}
									if obj[4]>0:
										# {"feature": "Occupation", "instances": 269, "metric_value": 0.4932, "depth": 10}
										if obj[5]<=19.604383225194468:
											# {"feature": "Bar", "instances": 252, "metric_value": 0.4975, "depth": 11}
											if obj[6]>-1.0:
												return 'False'
											elif obj[6]<=-1.0:
												return 'True'
											else: return 'True'
										elif obj[5]>19.604383225194468:
											# {"feature": "Bar", "instances": 17, "metric_value": 0.3975, "depth": 11}
											if obj[6]<=1.0:
												return 'False'
											elif obj[6]>1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										# {"feature": "Occupation", "instances": 159, "metric_value": 0.4915, "depth": 10}
										if obj[5]<=6:
											# {"feature": "Bar", "instances": 93, "metric_value": 0.4909, "depth": 11}
											if obj[6]>-1.0:
												return 'False'
											elif obj[6]<=-1.0:
												return 'True'
											else: return 'True'
										elif obj[5]>6:
											# {"feature": "Bar", "instances": 66, "metric_value": 0.4532, "depth": 11}
											if obj[6]<=2.0:
												return 'True'
											elif obj[6]>2.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[3]>6:
									# {"feature": "Occupation", "instances": 26, "metric_value": 0.3798, "depth": 9}
									if obj[5]>5:
										# {"feature": "Education", "instances": 16, "metric_value": 0.2167, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Bar", "instances": 15, "metric_value": 0.2111, "depth": 11}
											if obj[6]<=1.0:
												return 'False'
											elif obj[6]>1.0:
												return 'False'
											else: return 'False'
										elif obj[4]>3:
											return 'True'
										else: return 'True'
									elif obj[5]<=5:
										# {"feature": "Education", "instances": 10, "metric_value": 0.5, "depth": 10}
										if obj[4]>0:
											# {"feature": "Bar", "instances": 6, "metric_value": 0.5, "depth": 11}
											if obj[6]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[6]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[1]>1:
							# {"feature": "Age", "instances": 622, "metric_value": 0.4838, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Occupation", "instances": 344, "metric_value": 0.4909, "depth": 8}
								if obj[5]<=8.069767441860465:
									# {"feature": "Bar", "instances": 195, "metric_value": 0.4717, "depth": 9}
									if obj[6]>-1.0:
										# {"feature": "Education", "instances": 187, "metric_value": 0.4754, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Direction_same", "instances": 179, "metric_value": 0.4847, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[4]>3:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.1875, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]<=-1.0:
										# {"feature": "Education", "instances": 8, "metric_value": 0.125, "depth": 10}
										if obj[4]>0:
											return 'False'
										elif obj[4]<=0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]>8.069767441860465:
									# {"feature": "Bar", "instances": 149, "metric_value": 0.484, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Direction_same", "instances": 130, "metric_value": 0.4846, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Education", "instances": 99, "metric_value": 0.4965, "depth": 11}
											if obj[4]<=3:
												return 'True'
											elif obj[4]>3:
												return 'True'
											else: return 'True'
										elif obj[9]>0:
											# {"feature": "Education", "instances": 31, "metric_value": 0.3494, "depth": 11}
											if obj[4]>0:
												return 'False'
											elif obj[4]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[6]>2.0:
										# {"feature": "Direction_same", "instances": 19, "metric_value": 0.386, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Education", "instances": 16, "metric_value": 0.3571, "depth": 11}
											if obj[4]<=0:
												return 'False'
											elif obj[4]>0:
												return 'False'
											else: return 'False'
										elif obj[9]>0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[4]<=0:
												return 'False'
											elif obj[4]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>2:
								# {"feature": "Bar", "instances": 278, "metric_value": 0.4581, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Occupation", "instances": 142, "metric_value": 0.4778, "depth": 9}
									if obj[5]>4:
										# {"feature": "Education", "instances": 103, "metric_value": 0.4538, "depth": 10}
										if obj[4]>1:
											# {"feature": "Direction_same", "instances": 59, "metric_value": 0.4961, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[4]<=1:
											# {"feature": "Direction_same", "instances": 44, "metric_value": 0.3955, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]<=4:
										# {"feature": "Education", "instances": 39, "metric_value": 0.4661, "depth": 10}
										if obj[4]>0:
											# {"feature": "Direction_same", "instances": 23, "metric_value": 0.3794, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[4]<=0:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.3875, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]<=0.0:
									# {"feature": "Education", "instances": 136, "metric_value": 0.4207, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Occupation", "instances": 110, "metric_value": 0.4004, "depth": 10}
										if obj[5]<=12:
											# {"feature": "Direction_same", "instances": 95, "metric_value": 0.3875, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[5]>12:
											# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4571, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>2:
										# {"feature": "Direction_same", "instances": 26, "metric_value": 0.4733, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Occupation", "instances": 21, "metric_value": 0.4571, "depth": 11}
											if obj[5]<=11:
												return 'True'
											elif obj[5]>11:
												return 'True'
											else: return 'True'
										elif obj[9]>0:
											# {"feature": "Occupation", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[5]<=10:
												return 'True'
											elif obj[5]>10:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]>2.0:
						# {"feature": "Time", "instances": 55, "metric_value": 0.3433, "depth": 6}
						if obj[1]>0:
							# {"feature": "Age", "instances": 43, "metric_value": 0.3929, "depth": 7}
							if obj[3]>0:
								# {"feature": "Occupation", "instances": 28, "metric_value": 0.317, "depth": 8}
								if obj[5]<=6:
									# {"feature": "Direction_same", "instances": 17, "metric_value": 0.3975, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Education", "instances": 11, "metric_value": 0.4481, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Bar", "instances": 7, "metric_value": 0.4762, "depth": 11}
											if obj[6]<=1.0:
												return 'True'
											elif obj[6]>1.0:
												return 'True'
											else: return 'True'
										elif obj[4]>3:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[6]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[4]<=3:
											return 'True'
										elif obj[4]>3:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>6:
									# {"feature": "Education", "instances": 11, "metric_value": 0.1515, "depth": 9}
									if obj[4]>2:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[6]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[9]>0:
											return 'True'
										else: return 'True'
									elif obj[4]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Occupation", "instances": 15, "metric_value": 0.3143, "depth": 8}
								if obj[5]<=9:
									# {"feature": "Education", "instances": 8, "metric_value": 0.3571, "depth": 9}
									if obj[4]<=0:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4048, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[6]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[9]>0:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>0:
										return 'True'
									else: return 'True'
								elif obj[5]>9:
									# {"feature": "Education", "instances": 7, "metric_value": 0.2143, "depth": 9}
									if obj[4]<=0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=2.0:
												return 'False'
											else: return 'False'
										elif obj[9]>0:
											return 'False'
										else: return 'False'
									elif obj[4]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Age", "instances": 1090, "metric_value": 0.4589, "depth": 5}
					if obj[3]>1:
						# {"feature": "Bar", "instances": 692, "metric_value": 0.4712, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Occupation", "instances": 651, "metric_value": 0.469, "depth": 7}
							if obj[5]<=13.852614400462308:
								# {"feature": "Time", "instances": 550, "metric_value": 0.4754, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Restaurant20to50", "instances": 337, "metric_value": 0.4817, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Education", "instances": 267, "metric_value": 0.4864, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Direction_same", "instances": 244, "metric_value": 0.4959, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>3:
											# {"feature": "Direction_same", "instances": 23, "metric_value": 0.3856, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										# {"feature": "Education", "instances": 70, "metric_value": 0.431, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Direction_same", "instances": 67, "metric_value": 0.4304, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>3:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]>2:
									# {"feature": "Education", "instances": 213, "metric_value": 0.4513, "depth": 9}
									if obj[4]<=1:
										# {"feature": "Restaurant20to50", "instances": 111, "metric_value": 0.4163, "depth": 10}
										if obj[8]>-1.0:
											# {"feature": "Direction_same", "instances": 109, "metric_value": 0.4148, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]<=-1.0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>1:
										# {"feature": "Restaurant20to50", "instances": 102, "metric_value": 0.4842, "depth": 10}
										if obj[8]>-1.0:
											# {"feature": "Direction_same", "instances": 101, "metric_value": 0.489, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]<=-1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>13.852614400462308:
								# {"feature": "Education", "instances": 101, "metric_value": 0.4013, "depth": 8}
								if obj[4]>0:
									# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.4774, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Time", "instances": 47, "metric_value": 0.4602, "depth": 10}
										if obj[1]>0:
											# {"feature": "Direction_same", "instances": 40, "metric_value": 0.455, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[1]<=0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>1.0:
										# {"feature": "Time", "instances": 10, "metric_value": 0.32, "depth": 10}
										if obj[1]>2:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[1]<=2:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[4]<=0:
									# {"feature": "Time", "instances": 44, "metric_value": 0.2902, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.3359, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 24, "metric_value": 0.375, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>3:
										# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.15, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.18, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>2.0:
							# {"feature": "Occupation", "instances": 41, "metric_value": 0.4378, "depth": 7}
							if obj[5]>2:
								# {"feature": "Time", "instances": 39, "metric_value": 0.4438, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Education", "instances": 26, "metric_value": 0.483, "depth": 9}
									if obj[4]>0:
										# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.4978, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4978, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4481, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[8]>1.0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Education", "instances": 13, "metric_value": 0.3077, "depth": 9}
									if obj[4]>0:
										# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]<=2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]<=1:
						# {"feature": "Time", "instances": 398, "metric_value": 0.4216, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Restaurant20to50", "instances": 219, "metric_value": 0.4532, "depth": 7}
							if obj[8]<=1.0:
								# {"feature": "Occupation", "instances": 166, "metric_value": 0.4707, "depth": 8}
								if obj[5]<=20:
									# {"feature": "Bar", "instances": 157, "metric_value": 0.475, "depth": 9}
									if obj[6]>-1.0:
										# {"feature": "Education", "instances": 150, "metric_value": 0.4722, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Direction_same", "instances": 136, "metric_value": 0.4788, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>3:
											# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4082, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]<=-1.0:
										# {"feature": "Education", "instances": 7, "metric_value": 0.3429, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]>20:
									# {"feature": "Education", "instances": 9, "metric_value": 0.2963, "depth": 9}
									if obj[4]>0:
										# {"feature": "Bar", "instances": 6, "metric_value": 0.3333, "depth": 10}
										if obj[6]>0.0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[6]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]>1.0:
								# {"feature": "Bar", "instances": 53, "metric_value": 0.3608, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Education", "instances": 27, "metric_value": 0.2399, "depth": 9}
									if obj[4]>0:
										# {"feature": "Occupation", "instances": 21, "metric_value": 0.3031, "depth": 10}
										if obj[5]>1:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[5]<=1:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=0.0:
									# {"feature": "Education", "instances": 26, "metric_value": 0.4487, "depth": 9}
									if obj[4]<=3:
										# {"feature": "Occupation", "instances": 24, "metric_value": 0.4614, "depth": 10}
										if obj[5]<=12:
											# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4986, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[5]>12:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>3:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Occupation", "instances": 179, "metric_value": 0.3691, "depth": 7}
							if obj[5]<=7.189944134078212:
								# {"feature": "Bar", "instances": 116, "metric_value": 0.3172, "depth": 8}
								if obj[6]>-1.0:
									# {"feature": "Restaurant20to50", "instances": 115, "metric_value": 0.315, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Education", "instances": 82, "metric_value": 0.3517, "depth": 10}
										if obj[4]>1:
											# {"feature": "Direction_same", "instances": 48, "metric_value": 0.395, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]<=1:
											# {"feature": "Direction_same", "instances": 34, "metric_value": 0.2907, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										# {"feature": "Education", "instances": 33, "metric_value": 0.2027, "depth": 10}
										if obj[4]>0:
											# {"feature": "Direction_same", "instances": 18, "metric_value": 0.1049, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Direction_same", "instances": 15, "metric_value": 0.32, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[5]>7.189944134078212:
								# {"feature": "Bar", "instances": 63, "metric_value": 0.4194, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Education", "instances": 48, "metric_value": 0.3692, "depth": 9}
									if obj[4]>1:
										# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.4495, "depth": 10}
										if obj[8]>-1.0:
											# {"feature": "Direction_same", "instances": 30, "metric_value": 0.4644, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[4]<=1:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.1877, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Direction_same", "instances": 14, "metric_value": 0.1327, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>2.0:
									# {"feature": "Education", "instances": 15, "metric_value": 0.28, "depth": 9}
									if obj[4]<=0:
										# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.3, "depth": 10}
										if obj[8]<=0.0:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]>0.0:
											return 'True'
										else: return 'True'
									elif obj[4]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[10]>2:
				# {"feature": "Time", "instances": 292, "metric_value": 0.4475, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 244, "metric_value": 0.479, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Bar", "instances": 196, "metric_value": 0.4678, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Occupation", "instances": 99, "metric_value": 0.4188, "depth": 7}
							if obj[5]>1:
								# {"feature": "Age", "instances": 87, "metric_value": 0.3784, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.2726, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Passanger", "instances": 31, "metric_value": 0.1748, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 31, "metric_value": 0.1748, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>1.0:
										# {"feature": "Passanger", "instances": 19, "metric_value": 0.4321, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4321, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>3:
									# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.4787, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Passanger", "instances": 24, "metric_value": 0.4688, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4688, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>1.0:
										# {"feature": "Passanger", "instances": 13, "metric_value": 0.497, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[5]<=1:
								# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.35, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Age", "instances": 10, "metric_value": 0.4, "depth": 9}
									if obj[3]>0:
										# {"feature": "Passanger", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]<=0.0:
							# {"feature": "Age", "instances": 97, "metric_value": 0.461, "depth": 7}
							if obj[3]<=5:
								# {"feature": "Occupation", "instances": 80, "metric_value": 0.4795, "depth": 8}
								if obj[5]<=7:
									# {"feature": "Restaurant20to50", "instances": 49, "metric_value": 0.45, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Passanger", "instances": 37, "metric_value": 0.4383, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 37, "metric_value": 0.4383, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										# {"feature": "Passanger", "instances": 12, "metric_value": 0.4861, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]>7:
									# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.4739, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Passanger", "instances": 28, "metric_value": 0.477, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 28, "metric_value": 0.477, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>1.0:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[3]>5:
								# {"feature": "Occupation", "instances": 17, "metric_value": 0.2059, "depth": 8}
								if obj[5]<=9:
									# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.2136, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Passanger", "instances": 11, "metric_value": 0.1653, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1653, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>1.0:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]>9:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[4]>2:
						# {"feature": "Occupation", "instances": 48, "metric_value": 0.4574, "depth": 6}
						if obj[5]<=21:
							# {"feature": "Age", "instances": 45, "metric_value": 0.4522, "depth": 7}
							if obj[3]>0:
								# {"feature": "Bar", "instances": 40, "metric_value": 0.4487, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.4386, "depth": 9}
									if obj[8]>-1.0:
										# {"feature": "Passanger", "instances": 38, "metric_value": 0.4501, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 38, "metric_value": 0.4501, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[6]>1.0:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.2, "depth": 8}
								if obj[6]>0.0:
									return 'False'
								elif obj[6]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[8]>0.0:
										return 'True'
									elif obj[8]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[5]>21:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Passanger", "instances": 48, "metric_value": 0.0357, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						# {"feature": "Age", "instances": 7, "metric_value": 0.0, "depth": 6}
						if obj[3]<=5:
							return 'True'
						elif obj[3]>5:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[7]>1.0:
			# {"feature": "Distance", "instances": 2830, "metric_value": 0.4095, "depth": 3}
			if obj[10]<=2:
				# {"feature": "Passanger", "instances": 2559, "metric_value": 0.3976, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Occupation", "instances": 1657, "metric_value": 0.4189, "depth": 5}
					if obj[5]<=18.149362003525606:
						# {"feature": "Age", "instances": 1539, "metric_value": 0.4258, "depth": 6}
						if obj[3]>0:
							# {"feature": "Time", "instances": 1328, "metric_value": 0.4163, "depth": 7}
							if obj[1]>0:
								# {"feature": "Education", "instances": 941, "metric_value": 0.4312, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Bar", "instances": 891, "metric_value": 0.4275, "depth": 9}
									if obj[6]>0.0:
										# {"feature": "Restaurant20to50", "instances": 598, "metric_value": 0.4388, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 333, "metric_value": 0.4503, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											# {"feature": "Direction_same", "instances": 265, "metric_value": 0.4232, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]<=0.0:
										# {"feature": "Restaurant20to50", "instances": 293, "metric_value": 0.4012, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Direction_same", "instances": 254, "metric_value": 0.3921, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											# {"feature": "Direction_same", "instances": 39, "metric_value": 0.4581, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>3:
									# {"feature": "Bar", "instances": 50, "metric_value": 0.4716, "depth": 9}
									if obj[6]>0.0:
										# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4026, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.3175, "depth": 11}
											if obj[8]>0.0:
												return 'True'
											elif obj[8]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[9]>0:
											# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.404, "depth": 11}
											if obj[8]<=3.0:
												return 'True'
											elif obj[8]>3.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]<=0.0:
										# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.471, "depth": 10}
										if obj[8]<=0.0:
											# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3117, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[8]>0.0:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.45, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Direction_same", "instances": 387, "metric_value": 0.3679, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Bar", "instances": 239, "metric_value": 0.422, "depth": 9}
									if obj[6]>0.0:
										# {"feature": "Restaurant20to50", "instances": 162, "metric_value": 0.4494, "depth": 10}
										if obj[8]>-1.0:
											# {"feature": "Education", "instances": 160, "metric_value": 0.4535, "depth": 11}
											if obj[4]<=4:
												return 'True'
											elif obj[4]>4:
												return 'True'
											else: return 'True'
										elif obj[8]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[6]<=0.0:
										# {"feature": "Education", "instances": 77, "metric_value": 0.347, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.4176, "depth": 11}
											if obj[8]>0.0:
												return 'True'
											elif obj[8]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[4]>1:
											# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.2505, "depth": 11}
											if obj[8]>0.0:
												return 'True'
											elif obj[8]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]>0:
									# {"feature": "Restaurant20to50", "instances": 148, "metric_value": 0.2625, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Bar", "instances": 126, "metric_value": 0.2939, "depth": 10}
										if obj[6]<=2.0:
											# {"feature": "Education", "instances": 105, "metric_value": 0.253, "depth": 11}
											if obj[4]>1:
												return 'True'
											elif obj[4]<=1:
												return 'True'
											else: return 'True'
										elif obj[6]>2.0:
											# {"feature": "Education", "instances": 21, "metric_value": 0.4512, "depth": 11}
											if obj[4]>1:
												return 'True'
											elif obj[4]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>2.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Education", "instances": 211, "metric_value": 0.4526, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Restaurant20to50", "instances": 184, "metric_value": 0.4785, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Bar", "instances": 148, "metric_value": 0.4591, "depth": 9}
									if obj[6]<=3.0:
										# {"feature": "Direction_same", "instances": 140, "metric_value": 0.4746, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Time", "instances": 87, "metric_value": 0.4888, "depth": 11}
											if obj[1]>0:
												return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										elif obj[9]>0:
											# {"feature": "Time", "instances": 53, "metric_value": 0.4322, "depth": 11}
											if obj[1]<=1:
												return 'True'
											elif obj[1]>1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>3.0:
										return 'True'
									else: return 'True'
								elif obj[8]>2.0:
									# {"feature": "Bar", "instances": 36, "metric_value": 0.4167, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Time", "instances": 30, "metric_value": 0.4643, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.45, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[1]>1:
											# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4589, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>2.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]>3:
								# {"feature": "Direction_same", "instances": 27, "metric_value": 0.1882, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Time", "instances": 17, "metric_value": 0.1046, "depth": 9}
									if obj[1]>2:
										# {"feature": "Bar", "instances": 9, "metric_value": 0.1905, "depth": 10}
										if obj[6]<=0.0:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2381, "depth": 11}
											if obj[8]<=1.0:
												return 'True'
											elif obj[8]>1.0:
												return 'True'
											else: return 'True'
										elif obj[6]>0.0:
											return 'True'
										else: return 'True'
									elif obj[1]<=2:
										return 'True'
									else: return 'True'
								elif obj[9]>0:
									# {"feature": "Time", "instances": 10, "metric_value": 0.2667, "depth": 9}
									if obj[1]>0:
										# {"feature": "Bar", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[6]<=2.0:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[8]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[6]>2.0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[5]>18.149362003525606:
						# {"feature": "Time", "instances": 118, "metric_value": 0.2949, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Age", "instances": 71, "metric_value": 0.3361, "depth": 7}
							if obj[3]>0:
								# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.4015, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Education", "instances": 52, "metric_value": 0.4294, "depth": 9}
									if obj[4]>0:
										# {"feature": "Bar", "instances": 31, "metric_value": 0.4508, "depth": 10}
										if obj[6]<=1.0:
											# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4316, "depth": 11}
											if obj[9]>0:
												return 'True'
											elif obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[6]>1.0:
											# {"feature": "Direction_same", "instances": 12, "metric_value": 0.3333, "depth": 11}
											if obj[9]>0:
												return 'True'
											elif obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										# {"feature": "Bar", "instances": 21, "metric_value": 0.3464, "depth": 10}
										if obj[6]<=2.0:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.2792, "depth": 11}
											if obj[9]>0:
												return 'True'
											elif obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]>2.0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[9]>0:
												return 'False'
											elif obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>2.0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							# {"feature": "Bar", "instances": 47, "metric_value": 0.1789, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Direction_same", "instances": 40, "metric_value": 0.1152, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Age", "instances": 34, "metric_value": 0.0515, "depth": 9}
									if obj[3]>0:
										return 'True'
									elif obj[3]<=0:
										# {"feature": "Education", "instances": 8, "metric_value": 0.125, "depth": 10}
										if obj[4]<=2:
											return 'True'
										elif obj[4]>2:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[8]<=1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]>0:
									# {"feature": "Education", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[4]<=0:
										return 'True'
									elif obj[4]>0:
										# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[8]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]>2.0:
								# {"feature": "Age", "instances": 7, "metric_value": 0.2857, "depth": 8}
								if obj[3]>0:
									# {"feature": "Education", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[4]<=0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>0:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Bar", "instances": 902, "metric_value": 0.349, "depth": 5}
					if obj[6]<=3.0:
						# {"feature": "Education", "instances": 848, "metric_value": 0.3366, "depth": 6}
						if obj[4]<=3:
							# {"feature": "Time", "instances": 804, "metric_value": 0.3474, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Occupation", "instances": 489, "metric_value": 0.3124, "depth": 8}
								if obj[5]>2.5454774682183086:
									# {"feature": "Restaurant20to50", "instances": 406, "metric_value": 0.334, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Age", "instances": 370, "metric_value": 0.3205, "depth": 10}
										if obj[3]<=6:
											# {"feature": "Direction_same", "instances": 358, "metric_value": 0.3312, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[3]>6:
											return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										# {"feature": "Age", "instances": 36, "metric_value": 0.4308, "depth": 10}
										if obj[3]<=4:
											# {"feature": "Direction_same", "instances": 26, "metric_value": 0.4734, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[3]>4:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=2.5454774682183086:
									# {"feature": "Age", "instances": 83, "metric_value": 0.1624, "depth": 9}
									if obj[3]<=6:
										# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.1414, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Direction_same", "instances": 74, "metric_value": 0.149, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											return 'True'
										else: return 'True'
									elif obj[3]>6:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Age", "instances": 315, "metric_value": 0.3837, "depth": 8}
								if obj[3]>0:
									# {"feature": "Restaurant20to50", "instances": 279, "metric_value": 0.3631, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Occupation", "instances": 163, "metric_value": 0.4061, "depth": 10}
										if obj[5]<=7.3128834355828225:
											# {"feature": "Direction_same", "instances": 109, "metric_value": 0.436, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[5]>7.3128834355828225:
											# {"feature": "Direction_same", "instances": 54, "metric_value": 0.3457, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										# {"feature": "Occupation", "instances": 116, "metric_value": 0.2909, "depth": 10}
										if obj[5]<=19:
											# {"feature": "Direction_same", "instances": 108, "metric_value": 0.2778, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[5]>19:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Occupation", "instances": 36, "metric_value": 0.4375, "depth": 9}
									if obj[5]<=10:
										# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.4643, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Direction_same", "instances": 28, "metric_value": 0.477, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>10:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[4]>3:
							# {"feature": "Time", "instances": 44, "metric_value": 0.0744, "depth": 7}
							if obj[1]<=3:
								return 'True'
							elif obj[1]>3:
								# {"feature": "Age", "instances": 11, "metric_value": 0.1636, "depth": 8}
								if obj[3]<=4:
									# {"feature": "Occupation", "instances": 10, "metric_value": 0.1333, "depth": 9}
									if obj[5]>1:
										return 'True'
									elif obj[5]<=1:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[8]>1.0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[8]<=1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>4:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[6]>3.0:
						# {"feature": "Time", "instances": 54, "metric_value": 0.4364, "depth": 6}
						if obj[1]>0:
							# {"feature": "Age", "instances": 44, "metric_value": 0.43, "depth": 7}
							if obj[3]>0:
								# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.4762, "depth": 8}
								if obj[8]>2.0:
									# {"feature": "Education", "instances": 20, "metric_value": 0.4945, "depth": 9}
									if obj[4]>0:
										# {"feature": "Occupation", "instances": 13, "metric_value": 0.4965, "depth": 10}
										if obj[5]<=1:
											# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[5]>1:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										# {"feature": "Occupation", "instances": 7, "metric_value": 0.4898, "depth": 10}
										if obj[5]<=14:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]<=2.0:
									# {"feature": "Occupation", "instances": 15, "metric_value": 0.4242, "depth": 9}
									if obj[5]<=7:
										# {"feature": "Education", "instances": 11, "metric_value": 0.3697, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>7:
										# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Occupation", "instances": 9, "metric_value": 0.0, "depth": 8}
								if obj[5]<=12:
									return 'True'
								elif obj[5]>12:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Age", "instances": 10, "metric_value": 0.1778, "depth": 7}
							if obj[3]<=4:
								# {"feature": "Education", "instances": 9, "metric_value": 0.1667, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									# {"feature": "Occupation", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[5]<=7:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[8]<=0.0:
											return 'False'
										elif obj[8]>0.0:
											return 'True'
										else: return 'True'
									elif obj[5]>7:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>4:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[10]>2:
				# {"feature": "Age", "instances": 271, "metric_value": 0.4863, "depth": 4}
				if obj[3]<=5:
					# {"feature": "Passanger", "instances": 227, "metric_value": 0.4831, "depth": 5}
					if obj[0]>0:
						# {"feature": "Occupation", "instances": 220, "metric_value": 0.4853, "depth": 6}
						if obj[5]<=11.96483872460614:
							# {"feature": "Time", "instances": 185, "metric_value": 0.4917, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Restaurant20to50", "instances": 146, "metric_value": 0.4785, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Bar", "instances": 130, "metric_value": 0.4925, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Education", "instances": 101, "metric_value": 0.497, "depth": 10}
										if obj[4]>1:
											# {"feature": "Direction_same", "instances": 62, "metric_value": 0.4953, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]<=1:
											# {"feature": "Direction_same", "instances": 39, "metric_value": 0.4997, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>2.0:
										# {"feature": "Education", "instances": 29, "metric_value": 0.4429, "depth": 10}
										if obj[4]>1:
											# {"feature": "Direction_same", "instances": 20, "metric_value": 0.42, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]<=1:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]>2.0:
									# {"feature": "Education", "instances": 16, "metric_value": 0.0, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]>1:
								# {"feature": "Education", "instances": 39, "metric_value": 0.4386, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.4578, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Bar", "instances": 20, "metric_value": 0.4088, "depth": 10}
										if obj[6]>0.0:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]<=0.0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										# {"feature": "Bar", "instances": 11, "metric_value": 0.3939, "depth": 10}
										if obj[6]<=1.0:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[6]>1.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[4]>3:
									# {"feature": "Bar", "instances": 8, "metric_value": 0.1875, "depth": 9}
									if obj[6]>0.0:
										return 'True'
									elif obj[6]<=0.0:
										# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>11.96483872460614:
							# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.3469, "depth": 7}
							if obj[8]<=1.0:
								# {"feature": "Education", "instances": 21, "metric_value": 0.2143, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Time", "instances": 12, "metric_value": 0.2727, "depth": 9}
									if obj[1]>0:
										# {"feature": "Bar", "instances": 11, "metric_value": 0.2727, "depth": 10}
										if obj[6]<=2.0:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]>2.0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[4]>2:
									return 'True'
								else: return 'True'
							elif obj[8]>1.0:
								# {"feature": "Time", "instances": 14, "metric_value": 0.4167, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Education", "instances": 12, "metric_value": 0.4381, "depth": 9}
									if obj[4]>1:
										# {"feature": "Bar", "instances": 7, "metric_value": 0.3429, "depth": 10}
										if obj[6]>1.0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[4]<=1:
										# {"feature": "Bar", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[6]<=2.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]>2.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>5:
					# {"feature": "Education", "instances": 44, "metric_value": 0.3598, "depth": 5}
					if obj[4]>0:
						# {"feature": "Occupation", "instances": 31, "metric_value": 0.2688, "depth": 6}
						if obj[5]<=16:
							# {"feature": "Bar", "instances": 30, "metric_value": 0.2299, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.2146, "depth": 8}
								if obj[8]>1.0:
									# {"feature": "Time", "instances": 18, "metric_value": 0.3333, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Passanger", "instances": 16, "metric_value": 0.3667, "depth": 10}
										if obj[0]>0:
											# {"feature": "Direction_same", "instances": 15, "metric_value": 0.3911, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								elif obj[8]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[6]>2.0:
								return 'True'
							else: return 'True'
						elif obj[5]>16:
							return 'True'
						else: return 'True'
					elif obj[4]<=0:
						# {"feature": "Time", "instances": 13, "metric_value": 0.2462, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Bar", "instances": 10, "metric_value": 0.1333, "depth": 7}
							if obj[6]<=0.0:
								return 'True'
							elif obj[6]>0.0:
								# {"feature": "Occupation", "instances": 3, "metric_value": 0.3333, "depth": 8}
								if obj[5]>6:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[8]<=1.0:
										return 'True'
									elif obj[8]>1.0:
										return 'False'
									else: return 'False'
								elif obj[5]<=6:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2260, "metric_value": 0.4558, "depth": 2}
		if obj[6]<=1.0:
			# {"feature": "Occupation", "instances": 1577, "metric_value": 0.4395, "depth": 3}
			if obj[5]>1.8509661496426837:
				# {"feature": "Education", "instances": 1312, "metric_value": 0.4571, "depth": 4}
				if obj[4]>0:
					# {"feature": "Coffeehouse", "instances": 846, "metric_value": 0.4314, "depth": 5}
					if obj[7]<=3.0:
						# {"feature": "Restaurant20to50", "instances": 795, "metric_value": 0.441, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Passanger", "instances": 570, "metric_value": 0.4164, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Time", "instances": 490, "metric_value": 0.3949, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Distance", "instances": 330, "metric_value": 0.4363, "depth": 9}
									if obj[10]<=2:
										# {"feature": "Age", "instances": 242, "metric_value": 0.4578, "depth": 10}
										if obj[3]<=6:
											# {"feature": "Direction_same", "instances": 230, "metric_value": 0.4562, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[3]>6:
											# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4792, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>2:
										# {"feature": "Age", "instances": 88, "metric_value": 0.3543, "depth": 10}
										if obj[3]<=4:
											# {"feature": "Direction_same", "instances": 75, "metric_value": 0.3911, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[3]>4:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.142, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Age", "instances": 160, "metric_value": 0.2917, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Distance", "instances": 109, "metric_value": 0.2443, "depth": 10}
										if obj[10]<=2:
											# {"feature": "Direction_same", "instances": 104, "metric_value": 0.2329, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[10]>2:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]>3:
										# {"feature": "Distance", "instances": 51, "metric_value": 0.3717, "depth": 10}
										if obj[10]<=2:
											# {"feature": "Direction_same", "instances": 48, "metric_value": 0.3938, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[10]>2:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>2:
								# {"feature": "Time", "instances": 80, "metric_value": 0.4795, "depth": 8}
								if obj[1]>0:
									# {"feature": "Age", "instances": 78, "metric_value": 0.4854, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Distance", "instances": 44, "metric_value": 0.4724, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4669, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[10]<=1:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]>2:
										# {"feature": "Distance", "instances": 34, "metric_value": 0.4966, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4994, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[10]<=1:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[8]>1.0:
							# {"feature": "Age", "instances": 225, "metric_value": 0.4756, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Passanger", "instances": 113, "metric_value": 0.4489, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 78, "metric_value": 0.4559, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Distance", "instances": 48, "metric_value": 0.423, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 38, "metric_value": 0.4501, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[10]<=1:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 11}
											if obj[9]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]>1:
										# {"feature": "Direction_same", "instances": 30, "metric_value": 0.4828, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 29, "metric_value": 0.4991, "depth": 11}
											if obj[10]<=1:
												return 'False'
											elif obj[10]>1:
												return 'False'
											else: return 'False'
										elif obj[9]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[0]>1:
									# {"feature": "Direction_same", "instances": 35, "metric_value": 0.381, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Time", "instances": 32, "metric_value": 0.3417, "depth": 10}
										if obj[1]>2:
											# {"feature": "Distance", "instances": 20, "metric_value": 0.25, "depth": 11}
											if obj[10]>1:
												return 'False'
											elif obj[10]<=1:
												return 'False'
											else: return 'False'
										elif obj[1]<=2:
											# {"feature": "Distance", "instances": 12, "metric_value": 0.4167, "depth": 11}
											if obj[10]>1:
												return 'True'
											elif obj[10]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>0:
										# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[1]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[10]<=2:
												return 'True'
											else: return 'True'
										elif obj[1]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[3]>2:
								# {"feature": "Time", "instances": 112, "metric_value": 0.4817, "depth": 8}
								if obj[1]>0:
									# {"feature": "Passanger", "instances": 77, "metric_value": 0.4521, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Distance", "instances": 59, "metric_value": 0.4555, "depth": 10}
										if obj[10]<=2:
											# {"feature": "Direction_same", "instances": 49, "metric_value": 0.4806, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[10]>2:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]>2:
										# {"feature": "Distance", "instances": 18, "metric_value": 0.3819, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4297, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Passanger", "instances": 35, "metric_value": 0.402, "depth": 9}
									if obj[0]>0:
										# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4307, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 16, "metric_value": 0.4667, "depth": 11}
											if obj[10]>1:
												return 'False'
											elif obj[10]<=1:
												return 'False'
											else: return 'False'
										elif obj[9]>0:
											# {"feature": "Distance", "instances": 13, "metric_value": 0.3462, "depth": 11}
											if obj[10]<=1:
												return 'True'
											elif obj[10]>1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]>3.0:
						# {"feature": "Distance", "instances": 51, "metric_value": 0.1696, "depth": 6}
						if obj[10]<=2:
							# {"feature": "Time", "instances": 37, "metric_value": 0.2194, "depth": 7}
							if obj[1]>2:
								# {"feature": "Age", "instances": 19, "metric_value": 0.0789, "depth": 8}
								if obj[3]>1:
									return 'False'
								elif obj[3]<=1:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]<=2:
								# {"feature": "Age", "instances": 18, "metric_value": 0.3175, "depth": 8}
								if obj[3]<=4:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.381, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Passanger", "instances": 12, "metric_value": 0.4333, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4167, "depth": 11}
											if obj[9]>0:
												return 'False'
											elif obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[0]>2:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[3]>4:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[10]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]<=0:
					# {"feature": "Age", "instances": 466, "metric_value": 0.4869, "depth": 5}
					if obj[3]>2:
						# {"feature": "Coffeehouse", "instances": 296, "metric_value": 0.488, "depth": 6}
						if obj[7]<=3.0:
							# {"feature": "Restaurant20to50", "instances": 260, "metric_value": 0.4892, "depth": 7}
							if obj[8]<=2.0:
								# {"feature": "Distance", "instances": 248, "metric_value": 0.4956, "depth": 8}
								if obj[10]<=2:
									# {"feature": "Time", "instances": 202, "metric_value": 0.493, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Passanger", "instances": 148, "metric_value": 0.4945, "depth": 10}
										if obj[0]>0:
											# {"feature": "Direction_same", "instances": 134, "metric_value": 0.4976, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[0]<=0:
											# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4592, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>3:
										# {"feature": "Passanger", "instances": 54, "metric_value": 0.4802, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Direction_same", "instances": 39, "metric_value": 0.4734, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[0]>2:
											# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4978, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]>2:
									# {"feature": "Time", "instances": 46, "metric_value": 0.4647, "depth": 9}
									if obj[1]>0:
										# {"feature": "Passanger", "instances": 39, "metric_value": 0.4557, "depth": 10}
										if obj[0]>0:
											# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4506, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[0]<=0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Passanger", "instances": 7, "metric_value": 0.4898, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[8]>2.0:
								# {"feature": "Passanger", "instances": 12, "metric_value": 0.2381, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Distance", "instances": 7, "metric_value": 0.2857, "depth": 9}
									if obj[10]>1:
										# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									elif obj[10]<=1:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>3.0:
							# {"feature": "Distance", "instances": 36, "metric_value": 0.3815, "depth": 7}
							if obj[10]<=2:
								# {"feature": "Passanger", "instances": 30, "metric_value": 0.3359, "depth": 8}
								if obj[0]>0:
									# {"feature": "Direction_same", "instances": 26, "metric_value": 0.2896, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.1925, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Time", "instances": 11, "metric_value": 0.2597, "depth": 11}
											if obj[1]<=3:
												return 'False'
											elif obj[1]>3:
												return 'False'
											else: return 'False'
										elif obj[8]>1.0:
											return 'False'
										else: return 'False'
									elif obj[9]>0:
										# {"feature": "Time", "instances": 9, "metric_value": 0.4167, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.3571, "depth": 11}
											if obj[8]<=2.0:
												return 'False'
											elif obj[8]>2.0:
												return 'True'
											else: return 'True'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[0]<=0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[1]>0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[10]>2:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.4, "depth": 8}
								if obj[0]>0:
									# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[1]<=0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[8]<=1.0:
											return 'False'
										elif obj[8]>1.0:
											return 'True'
										else: return 'True'
									elif obj[1]>0:
										return 'True'
									else: return 'True'
								elif obj[0]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=2:
						# {"feature": "Passanger", "instances": 170, "metric_value": 0.4518, "depth": 6}
						if obj[0]>0:
							# {"feature": "Time", "instances": 137, "metric_value": 0.4186, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Direction_same", "instances": 119, "metric_value": 0.4507, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Coffeehouse", "instances": 94, "metric_value": 0.4556, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Restaurant20to50", "instances": 67, "metric_value": 0.4853, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Distance", "instances": 46, "metric_value": 0.4895, "depth": 11}
											if obj[10]<=2:
												return 'False'
											elif obj[10]>2:
												return 'False'
											else: return 'False'
										elif obj[8]>1.0:
											# {"feature": "Distance", "instances": 21, "metric_value": 0.4542, "depth": 11}
											if obj[10]<=2:
												return 'True'
											elif obj[10]>2:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Distance", "instances": 27, "metric_value": 0.3188, "depth": 10}
										if obj[10]>1:
											# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.2783, "depth": 11}
											if obj[8]>0.0:
												return 'False'
											elif obj[8]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[10]<=1:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[8]<=1.0:
												return 'True'
											elif obj[8]>1.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[9]>0:
									# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.3, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.2438, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Distance", "instances": 16, "metric_value": 0.3021, "depth": 11}
											if obj[10]<=1:
												return 'False'
											elif obj[10]>1:
												return 'False'
											else: return 'False'
										elif obj[8]>1.0:
											return 'False'
										else: return 'False'
									elif obj[7]>1.0:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[8]>1.0:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=1:
												return 'True'
											else: return 'True'
										elif obj[8]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]>3:
								# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.0556, "depth": 8}
								if obj[7]>-1.0:
									return 'False'
								elif obj[7]<=-1.0:
									# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[10]>1:
										return 'False'
									elif obj[10]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[0]<=0:
							# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.4692, "depth": 7}
							if obj[7]>-1.0:
								# {"feature": "Time", "instances": 31, "metric_value": 0.4809, "depth": 8}
								if obj[1]>2:
									# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.4762, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Distance", "instances": 21, "metric_value": 0.4893, "depth": 10}
										if obj[10]<=1:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4922, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[10]>1:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[1]<=2:
									# {"feature": "Distance", "instances": 9, "metric_value": 0.381, "depth": 9}
									if obj[10]>1:
										# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.4762, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]<=-1.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[5]<=1.8509661496426837:
				# {"feature": "Restaurant20to50", "instances": 265, "metric_value": 0.3153, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "Distance", "instances": 216, "metric_value": 0.3556, "depth": 5}
					if obj[10]<=2:
						# {"feature": "Coffeehouse", "instances": 177, "metric_value": 0.3768, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Age", "instances": 102, "metric_value": 0.2838, "depth": 7}
							if obj[3]>1:
								# {"feature": "Education", "instances": 79, "metric_value": 0.2187, "depth": 8}
								if obj[4]>0:
									# {"feature": "Passanger", "instances": 50, "metric_value": 0.1759, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 31, "metric_value": 0.1182, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Direction_same", "instances": 23, "metric_value": 0.0812, "depth": 11}
											if obj[9]>0:
												return 'False'
											elif obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[1]>3:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]>1:
										# {"feature": "Time", "instances": 19, "metric_value": 0.1871, "depth": 10}
										if obj[1]>2:
											# {"feature": "Direction_same", "instances": 18, "metric_value": 0.1597, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[1]<=2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[4]<=0:
									# {"feature": "Passanger", "instances": 29, "metric_value": 0.251, "depth": 9}
									if obj[0]>0:
										# {"feature": "Time", "instances": 25, "metric_value": 0.195, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.2625, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[1]>2:
											return 'False'
										else: return 'False'
									elif obj[0]<=0:
										# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[1]>0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]<=1:
								# {"feature": "Time", "instances": 23, "metric_value": 0.4415, "depth": 8}
								if obj[1]>0:
									# {"feature": "Passanger", "instances": 18, "metric_value": 0.4008, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Education", "instances": 14, "metric_value": 0.3636, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4545, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[4]>3:
											return 'False'
										else: return 'False'
									elif obj[0]>2:
										# {"feature": "Education", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Education", "instances": 5, "metric_value": 0.0, "depth": 9}
									if obj[4]>0:
										return 'True'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[7]>1.0:
							# {"feature": "Education", "instances": 75, "metric_value": 0.3927, "depth": 7}
							if obj[4]>0:
								# {"feature": "Age", "instances": 55, "metric_value": 0.3449, "depth": 8}
								if obj[3]>2:
									# {"feature": "Time", "instances": 32, "metric_value": 0.4042, "depth": 9}
									if obj[1]>1:
										# {"feature": "Passanger", "instances": 20, "metric_value": 0.4768, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4628, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[0]>2:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=1:
										# {"feature": "Passanger", "instances": 12, "metric_value": 0.2727, "depth": 10}
										if obj[0]>0:
											# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2922, "depth": 11}
											if obj[9]>0:
												return 'False'
											elif obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]<=2:
									# {"feature": "Direction_same", "instances": 23, "metric_value": 0.2057, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Passanger", "instances": 16, "metric_value": 0.1071, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											# {"feature": "Time", "instances": 7, "metric_value": 0.2143, "depth": 11}
											if obj[1]>0:
												return 'False'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>0:
										# {"feature": "Passanger", "instances": 7, "metric_value": 0.3714, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[1]>0:
												return 'False'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]<=0:
								# {"feature": "Age", "instances": 20, "metric_value": 0.3792, "depth": 8}
								if obj[3]<=4:
									# {"feature": "Time", "instances": 12, "metric_value": 0.3611, "depth": 9}
									if obj[1]>2:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[0]>1:
											return 'False'
										elif obj[0]<=1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=2:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.3333, "depth": 10}
										if obj[0]>1:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[0]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>4:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.1667, "depth": 9}
									if obj[9]<=0:
										return 'True'
									elif obj[9]>0:
										# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[1]<=0:
											# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												return 'True'
											else: return 'True'
										elif obj[1]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[10]>2:
						# {"feature": "Passanger", "instances": 39, "metric_value": 0.1835, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coffeehouse", "instances": 38, "metric_value": 0.1655, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Education", "instances": 27, "metric_value": 0.0684, "depth": 8}
								if obj[4]<=1:
									return 'False'
								elif obj[4]>1:
									# {"feature": "Age", "instances": 13, "metric_value": 0.1346, "depth": 9}
									if obj[3]>2:
										# {"feature": "Time", "instances": 8, "metric_value": 0.2083, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									elif obj[3]<=2:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]<=0.0:
								# {"feature": "Age", "instances": 11, "metric_value": 0.2727, "depth": 8}
								if obj[3]>4:
									# {"feature": "Time", "instances": 6, "metric_value": 0.4, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Education", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								elif obj[3]<=4:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[8]<=0.0:
					# {"feature": "Age", "instances": 49, "metric_value": 0.049, "depth": 5}
					if obj[3]<=6:
						return 'False'
					elif obj[3]>6:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.2667, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 7}
							if obj[1]>0:
								# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[4]<=5:
									# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[10]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[6]>1.0:
			# {"feature": "Restaurant20to50", "instances": 683, "metric_value": 0.4668, "depth": 3}
			if obj[8]<=2.0:
				# {"feature": "Passanger", "instances": 562, "metric_value": 0.4802, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Time", "instances": 474, "metric_value": 0.486, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Occupation", "instances": 308, "metric_value": 0.4768, "depth": 6}
						if obj[5]>0:
							# {"feature": "Direction_same", "instances": 304, "metric_value": 0.4789, "depth": 7}
							if obj[9]<=0:
								# {"feature": "Age", "instances": 215, "metric_value": 0.4818, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Distance", "instances": 122, "metric_value": 0.4885, "depth": 9}
									if obj[10]>1:
										# {"feature": "Education", "instances": 116, "metric_value": 0.4922, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Coffeehouse", "instances": 111, "metric_value": 0.4963, "depth": 11}
											if obj[7]<=2.0:
												return 'True'
											elif obj[7]>2.0:
												return 'False'
											else: return 'False'
										elif obj[4]>3:
											# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[7]<=0.0:
												return 'True'
											elif obj[7]>0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=1:
										# {"feature": "Education", "instances": 6, "metric_value": 0.1667, "depth": 10}
										if obj[4]>0:
											return 'False'
										elif obj[4]<=0:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[7]<=3.0:
												return 'False'
											elif obj[7]>3.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[3]>3:
									# {"feature": "Coffeehouse", "instances": 93, "metric_value": 0.4509, "depth": 9}
									if obj[7]<=3.0:
										# {"feature": "Distance", "instances": 79, "metric_value": 0.4511, "depth": 10}
										if obj[10]>1:
											# {"feature": "Education", "instances": 77, "metric_value": 0.4554, "depth": 11}
											if obj[4]<=3:
												return 'True'
											elif obj[4]>3:
												return 'False'
											else: return 'False'
										elif obj[10]<=1:
											return 'False'
										else: return 'False'
									elif obj[7]>3.0:
										# {"feature": "Education", "instances": 14, "metric_value": 0.3214, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Distance", "instances": 12, "metric_value": 0.3714, "depth": 11}
											if obj[10]<=2:
												return 'True'
											elif obj[10]>2:
												return 'True'
											else: return 'True'
										elif obj[4]>3:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[9]>0:
								# {"feature": "Coffeehouse", "instances": 89, "metric_value": 0.4305, "depth": 8}
								if obj[7]<=3.0:
									# {"feature": "Education", "instances": 81, "metric_value": 0.4194, "depth": 9}
									if obj[4]<=3:
										# {"feature": "Age", "instances": 78, "metric_value": 0.4302, "depth": 10}
										if obj[3]<=6:
											# {"feature": "Distance", "instances": 76, "metric_value": 0.4411, "depth": 11}
											if obj[10]<=1:
												return 'True'
											elif obj[10]>1:
												return 'True'
											else: return 'True'
										elif obj[3]>6:
											return 'True'
										else: return 'True'
									elif obj[4]>3:
										return 'True'
									else: return 'True'
								elif obj[7]>3.0:
									# {"feature": "Education", "instances": 8, "metric_value": 0.3, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Age", "instances": 5, "metric_value": 0.4667, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=1:
												return 'True'
											else: return 'True'
										elif obj[3]>1:
											# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[10]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>2:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						# {"feature": "Occupation", "instances": 166, "metric_value": 0.4852, "depth": 6}
						if obj[5]<=8.74698795180723:
							# {"feature": "Coffeehouse", "instances": 97, "metric_value": 0.4678, "depth": 7}
							if obj[7]>1.0:
								# {"feature": "Age", "instances": 61, "metric_value": 0.4514, "depth": 8}
								if obj[3]>1:
									# {"feature": "Education", "instances": 43, "metric_value": 0.4411, "depth": 9}
									if obj[4]>1:
										# {"feature": "Direction_same", "instances": 25, "metric_value": 0.3967, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 24, "metric_value": 0.4058, "depth": 11}
											if obj[10]<=2:
												return 'False'
											elif obj[10]>2:
												return 'False'
											else: return 'False'
										elif obj[9]>0:
											return 'False'
										else: return 'False'
									elif obj[4]<=1:
										# {"feature": "Distance", "instances": 18, "metric_value": 0.4618, "depth": 10}
										if obj[10]<=1:
											# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]>1:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]<=1:
									# {"feature": "Education", "instances": 18, "metric_value": 0.3333, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Distance", "instances": 16, "metric_value": 0.3667, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[10]<=1:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]<=1.0:
								# {"feature": "Education", "instances": 36, "metric_value": 0.3838, "depth": 8}
								if obj[4]>0:
									# {"feature": "Age", "instances": 25, "metric_value": 0.4528, "depth": 9}
									if obj[3]<=1:
										# {"feature": "Distance", "instances": 16, "metric_value": 0.3594, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[10]<=1:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]>1:
										# {"feature": "Distance", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[10]<=1:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]>1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Age", "instances": 11, "metric_value": 0.1364, "depth": 9}
									if obj[3]>1:
										return 'False'
									elif obj[3]<=1:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[10]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]>8.74698795180723:
							# {"feature": "Distance", "instances": 69, "metric_value": 0.4763, "depth": 7}
							if obj[10]<=1:
								# {"feature": "Age", "instances": 44, "metric_value": 0.4444, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.384, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Education", "instances": 15, "metric_value": 0.2923, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.2604, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>2:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Education", "instances": 10, "metric_value": 0.45, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>1:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.4258, "depth": 9}
									if obj[7]>1.0:
										# {"feature": "Education", "instances": 11, "metric_value": 0.404, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>2:
											return 'True'
										else: return 'True'
									elif obj[7]<=1.0:
										# {"feature": "Education", "instances": 8, "metric_value": 0.25, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[10]>1:
								# {"feature": "Education", "instances": 25, "metric_value": 0.4456, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Age", "instances": 19, "metric_value": 0.4653, "depth": 9}
									if obj[3]>1:
										# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.404, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[7]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[3]<=1:
										# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.375, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>2:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[7]>3.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[9]>0:
											return 'False'
										else: return 'False'
									elif obj[7]<=3.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 88, "metric_value": 0.3215, "depth": 5}
					if obj[1]>2:
						# {"feature": "Age", "instances": 67, "metric_value": 0.2508, "depth": 6}
						if obj[3]<=4:
							# {"feature": "Occupation", "instances": 64, "metric_value": 0.2299, "depth": 7}
							if obj[5]<=14:
								# {"feature": "Education", "instances": 50, "metric_value": 0.1746, "depth": 8}
								if obj[4]>1:
									# {"feature": "Distance", "instances": 27, "metric_value": 0.2469, "depth": 9}
									if obj[10]>1:
										# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.1905, "depth": 10}
										if obj[7]<=2.0:
											# {"feature": "Direction_same", "instances": 14, "metric_value": 0.2449, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[7]>2.0:
											return 'True'
										else: return 'True'
									elif obj[10]<=1:
										# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.2667, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=1:
									# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.0815, "depth": 9}
									if obj[7]>1.0:
										# {"feature": "Distance", "instances": 16, "metric_value": 0.1154, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.142, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]<=1:
											return 'True'
										else: return 'True'
									elif obj[7]<=1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>14:
								# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.3297, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.2564, "depth": 9}
									if obj[10]>1:
										# {"feature": "Education", "instances": 12, "metric_value": 0.2381, "depth": 10}
										if obj[4]>1:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									elif obj[10]<=1:
										return 'False'
									else: return 'False'
								elif obj[7]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[3]>4:
							# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 7}
							if obj[4]>0:
								return 'False'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]<=2:
						# {"feature": "Occupation", "instances": 21, "metric_value": 0.3079, "depth": 6}
						if obj[5]<=12:
							# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.28, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Education", "instances": 10, "metric_value": 0.375, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Age", "instances": 8, "metric_value": 0.3571, "depth": 9}
									if obj[3]>0:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.4082, "depth": 11}
											if obj[10]<=2:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]>2:
									return 'False'
								else: return 'False'
							elif obj[7]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[5]>12:
							# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 7}
							if obj[3]<=2:
								return 'True'
							elif obj[3]>2:
								# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 8}
								if obj[4]>0:
									# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[7]>0.0:
										return 'False'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[8]>2.0:
				# {"feature": "Age", "instances": 121, "metric_value": 0.343, "depth": 4}
				if obj[3]<=4:
					# {"feature": "Occupation", "instances": 108, "metric_value": 0.2892, "depth": 5}
					if obj[5]<=9:
						# {"feature": "Coffeehouse", "instances": 64, "metric_value": 0.1608, "depth": 6}
						if obj[7]<=3.0:
							# {"feature": "Distance", "instances": 43, "metric_value": 0.0851, "depth": 7}
							if obj[10]<=2:
								# {"feature": "Passanger", "instances": 36, "metric_value": 0.05, "depth": 8}
								if obj[0]<=2:
									return 'True'
								elif obj[0]>2:
									# {"feature": "Education", "instances": 10, "metric_value": 0.1714, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Time", "instances": 7, "metric_value": 0.2286, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[1]>3:
											return 'True'
										else: return 'True'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[10]>2:
								# {"feature": "Education", "instances": 7, "metric_value": 0.2143, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>3.0:
							# {"feature": "Distance", "instances": 21, "metric_value": 0.2665, "depth": 7}
							if obj[10]>1:
								# {"feature": "Passanger", "instances": 13, "metric_value": 0.0769, "depth": 8}
								if obj[0]<=2:
									return 'True'
								elif obj[0]>2:
									# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[4]<=4:
										return 'False'
									elif obj[4]>4:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[10]<=1:
								# {"feature": "Time", "instances": 8, "metric_value": 0.3, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[4]>3:
											# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												return 'True'
											else: return 'True'
										elif obj[4]<=3:
											return 'True'
										else: return 'True'
									elif obj[9]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[5]>9:
						# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.4211, "depth": 6}
						if obj[7]<=3.0:
							# {"feature": "Passanger", "instances": 38, "metric_value": 0.463, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Time", "instances": 29, "metric_value": 0.4497, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Education", "instances": 19, "metric_value": 0.4173, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Distance", "instances": 12, "metric_value": 0.35, "depth": 10}
										if obj[10]<=2:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4167, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[10]>2:
											return 'True'
										else: return 'True'
									elif obj[4]>2:
										# {"feature": "Distance", "instances": 7, "metric_value": 0.4286, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[10]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.3111, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Distance", "instances": 9, "metric_value": 0.1944, "depth": 10}
										if obj[10]<=2:
											# {"feature": "Education", "instances": 8, "metric_value": 0.1875, "depth": 11}
											if obj[4]>1:
												return 'False'
											elif obj[4]<=1:
												return 'False'
											else: return 'False'
										elif obj[10]>2:
											return 'True'
										else: return 'True'
									elif obj[9]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[0]>2:
								# {"feature": "Education", "instances": 9, "metric_value": 0.2667, "depth": 8}
								if obj[4]>0:
									# {"feature": "Time", "instances": 5, "metric_value": 0.4667, "depth": 9}
									if obj[1]>2:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=2:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=2:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[10]<=2:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>3.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>4:
					# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3916, "depth": 5}
					if obj[9]<=0:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.3697, "depth": 6}
						if obj[5]>5:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[5]<=5:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.0, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[9]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	else: return 'False'
