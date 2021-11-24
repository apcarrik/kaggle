def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4716, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5887, "metric_value": 0.4562, "depth": 2}
		if obj[6]<=1.0:
			# {"feature": "Distance", "instances": 3057, "metric_value": 0.4852, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Passanger", "instances": 2765, "metric_value": 0.4824, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 1675, "metric_value": 0.4929, "depth": 5}
					if obj[7]<=2.0:
						# {"feature": "Time", "instances": 1620, "metric_value": 0.4957, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Direction_same", "instances": 998, "metric_value": 0.4947, "depth": 7}
							if obj[8]>0:
								# {"feature": "Occupation", "instances": 544, "metric_value": 0.4879, "depth": 8}
								if obj[4]<=7.757352941176471:
									# {"feature": "Bar", "instances": 348, "metric_value": 0.4933, "depth": 9}
									if obj[5]>-1.0:
										# {"feature": "Education", "instances": 342, "metric_value": 0.4959, "depth": 10}
										if obj[3]<=2:
											return 'True'
										elif obj[3]>2:
											return 'False'
										else: return 'False'
									elif obj[5]<=-1.0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[3]>1:
											return 'False'
										elif obj[3]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]>7.757352941176471:
									# {"feature": "Education", "instances": 196, "metric_value": 0.4621, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Bar", "instances": 149, "metric_value": 0.4417, "depth": 10}
										if obj[5]<=1.0:
											return 'True'
										elif obj[5]>1.0:
											return 'True'
										else: return 'True'
									elif obj[3]>2:
										# {"feature": "Bar", "instances": 47, "metric_value": 0.4642, "depth": 10}
										if obj[5]<=1.0:
											return 'True'
										elif obj[5]>1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[8]<=0:
								# {"feature": "Occupation", "instances": 454, "metric_value": 0.4967, "depth": 8}
								if obj[4]<=19.996303730025073:
									# {"feature": "Bar", "instances": 419, "metric_value": 0.4976, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Education", "instances": 383, "metric_value": 0.4982, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										# {"feature": "Education", "instances": 36, "metric_value": 0.4692, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]>19.996303730025073:
									# {"feature": "Bar", "instances": 35, "metric_value": 0.4434, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Education", "instances": 25, "metric_value": 0.435, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0.0:
										# {"feature": "Education", "instances": 10, "metric_value": 0.3111, "depth": 10}
										if obj[3]<=2:
											return 'False'
										elif obj[3]>2:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]>1:
							# {"feature": "Occupation", "instances": 622, "metric_value": 0.4872, "depth": 7}
							if obj[4]<=20.08796747054774:
								# {"feature": "Direction_same", "instances": 585, "metric_value": 0.4906, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Bar", "instances": 461, "metric_value": 0.4852, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Education", "instances": 427, "metric_value": 0.4841, "depth": 10}
										if obj[3]<=3:
											return 'True'
										elif obj[3]>3:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										# {"feature": "Education", "instances": 34, "metric_value": 0.4287, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]>0:
									# {"feature": "Education", "instances": 124, "metric_value": 0.4719, "depth": 9}
									if obj[3]>0:
										# {"feature": "Bar", "instances": 85, "metric_value": 0.4804, "depth": 10}
										if obj[5]>-1.0:
											return 'False'
										elif obj[5]<=-1.0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Bar", "instances": 39, "metric_value": 0.4233, "depth": 10}
										if obj[5]<=0.0:
											return 'True'
										elif obj[5]>0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[4]>20.08796747054774:
								# {"feature": "Bar", "instances": 37, "metric_value": 0.3777, "depth": 8}
								if obj[5]>0.0:
									# {"feature": "Direction_same", "instances": 21, "metric_value": 0.2993, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Education", "instances": 14, "metric_value": 0.2251, "depth": 10}
										if obj[3]<=2:
											return 'True'
										elif obj[3]>2:
											return 'True'
										else: return 'True'
									elif obj[8]>0:
										# {"feature": "Education", "instances": 7, "metric_value": 0.1905, "depth": 10}
										if obj[3]>2:
											return 'True'
										elif obj[3]<=2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[5]<=0.0:
									# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4583, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Education", "instances": 12, "metric_value": 0.3704, "depth": 10}
										if obj[3]<=1:
											return 'True'
										elif obj[3]>1:
											return 'True'
										else: return 'True'
									elif obj[8]>0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]>2.0:
						# {"feature": "Time", "instances": 55, "metric_value": 0.3433, "depth": 6}
						if obj[1]>0:
							# {"feature": "Occupation", "instances": 43, "metric_value": 0.3935, "depth": 7}
							if obj[4]<=9:
								# {"feature": "Direction_same", "instances": 33, "metric_value": 0.3636, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Bar", "instances": 22, "metric_value": 0.3883, "depth": 9}
									if obj[5]<=1.0:
										# {"feature": "Education", "instances": 16, "metric_value": 0.4219, "depth": 10}
										if obj[3]<=3:
											return 'True'
										elif obj[3]>3:
											return 'True'
										else: return 'True'
									elif obj[5]>1.0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[3]>1:
											return 'True'
										elif obj[3]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>0:
									# {"feature": "Education", "instances": 11, "metric_value": 0.2803, "depth": 9}
									if obj[3]>0:
										# {"feature": "Bar", "instances": 8, "metric_value": 0.2, "depth": 10}
										if obj[5]<=0.0:
											return 'True'
										elif obj[5]>0.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>9:
								# {"feature": "Education", "instances": 10, "metric_value": 0.3429, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Bar", "instances": 7, "metric_value": 0.2143, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[5]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Occupation", "instances": 1090, "metric_value": 0.4595, "depth": 5}
					if obj[4]>1.9446536028759107:
						# {"feature": "Bar", "instances": 918, "metric_value": 0.4679, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Education", "instances": 838, "metric_value": 0.4632, "depth": 7}
							if obj[3]>1:
								# {"feature": "Time", "instances": 470, "metric_value": 0.4744, "depth": 8}
								if obj[1]>0:
									# {"feature": "Restaurant20to50", "instances": 370, "metric_value": 0.4822, "depth": 9}
									if obj[7]>-1.0:
										# {"feature": "Direction_same", "instances": 363, "metric_value": 0.4868, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=-1.0:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Restaurant20to50", "instances": 100, "metric_value": 0.4321, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 76, "metric_value": 0.4501, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 24, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=1:
								# {"feature": "Restaurant20to50", "instances": 368, "metric_value": 0.4363, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Time", "instances": 301, "metric_value": 0.4593, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Direction_same", "instances": 175, "metric_value": 0.4822, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]>2:
										# {"feature": "Direction_same", "instances": 126, "metric_value": 0.4274, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									# {"feature": "Time", "instances": 67, "metric_value": 0.3109, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Direction_same", "instances": 36, "metric_value": 0.3457, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]>2:
										# {"feature": "Direction_same", "instances": 31, "metric_value": 0.2706, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>2.0:
							# {"feature": "Restaurant20to50", "instances": 80, "metric_value": 0.4795, "depth": 7}
							if obj[7]>1.0:
								# {"feature": "Time", "instances": 41, "metric_value": 0.4438, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Education", "instances": 27, "metric_value": 0.4742, "depth": 9}
									if obj[3]>0:
										# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4915, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Education", "instances": 14, "metric_value": 0.3117, "depth": 9}
									if obj[3]>1:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]<=1.0:
								# {"feature": "Time", "instances": 39, "metric_value": 0.4575, "depth": 8}
								if obj[1]>0:
									# {"feature": "Education", "instances": 30, "metric_value": 0.4897, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Direction_same", "instances": 26, "metric_value": 0.4882, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>2:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Education", "instances": 9, "metric_value": 0.2667, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]<=1.9446536028759107:
						# {"feature": "Time", "instances": 172, "metric_value": 0.3873, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Restaurant20to50", "instances": 99, "metric_value": 0.4402, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Education", "instances": 77, "metric_value": 0.4768, "depth": 8}
								if obj[3]<=4:
									# {"feature": "Bar", "instances": 76, "metric_value": 0.4786, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Direction_same", "instances": 75, "metric_value": 0.485, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										return 'True'
									else: return 'True'
								elif obj[3]>4:
									return 'True'
								else: return 'True'
							elif obj[7]>1.0:
								# {"feature": "Education", "instances": 22, "metric_value": 0.2657, "depth": 8}
								if obj[3]>0:
									# {"feature": "Bar", "instances": 13, "metric_value": 0.1346, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Bar", "instances": 9, "metric_value": 0.4167, "depth": 9}
									if obj[5]<=1.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Education", "instances": 73, "metric_value": 0.2905, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Bar", "instances": 38, "metric_value": 0.3263, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.3526, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 21, "metric_value": 0.3084, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>1.0:
									# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.1778, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>0:
								# {"feature": "Bar", "instances": 35, "metric_value": 0.2329, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.1543, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 17, "metric_value": 0.1107, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>1.0:
									# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.35, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[9]>2:
				# {"feature": "Time", "instances": 292, "metric_value": 0.4475, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 244, "metric_value": 0.479, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Bar", "instances": 196, "metric_value": 0.4678, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Occupation", "instances": 99, "metric_value": 0.4188, "depth": 7}
							if obj[4]>1:
								# {"feature": "Restaurant20to50", "instances": 87, "metric_value": 0.3931, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Passanger", "instances": 55, "metric_value": 0.3412, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 55, "metric_value": 0.3412, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>1.0:
									# {"feature": "Passanger", "instances": 32, "metric_value": 0.4824, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 32, "metric_value": 0.4824, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]<=1:
								# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.35, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Passanger", "instances": 10, "metric_value": 0.42, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]<=0.0:
							# {"feature": "Occupation", "instances": 97, "metric_value": 0.477, "depth": 7}
							if obj[4]>2:
								# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.4915, "depth": 8}
								if obj[7]>-1.0:
									# {"feature": "Passanger", "instances": 77, "metric_value": 0.4979, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 77, "metric_value": 0.4979, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[4]<=2:
								# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.3789, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "Passanger", "instances": 10, "metric_value": 0.32, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>0.0:
									# {"feature": "Passanger", "instances": 9, "metric_value": 0.4444, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]>2:
						# {"feature": "Occupation", "instances": 48, "metric_value": 0.4574, "depth": 6}
						if obj[4]<=21:
							# {"feature": "Bar", "instances": 45, "metric_value": 0.4568, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.4607, "depth": 8}
								if obj[7]>-1.0:
									# {"feature": "Passanger", "instances": 42, "metric_value": 0.4717, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 42, "metric_value": 0.4717, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[5]>1.0:
								return 'False'
							else: return 'False'
						elif obj[4]>21:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Passanger", "instances": 48, "metric_value": 0.0357, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						# {"feature": "Bar", "instances": 7, "metric_value": 0.0, "depth": 6}
						if obj[5]<=0.0:
							return 'True'
						elif obj[5]>0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[6]>1.0:
			# {"feature": "Distance", "instances": 2830, "metric_value": 0.4095, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Passanger", "instances": 2559, "metric_value": 0.3976, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Occupation", "instances": 1657, "metric_value": 0.4189, "depth": 5}
					if obj[4]<=18.149362003525606:
						# {"feature": "Time", "instances": 1539, "metric_value": 0.4266, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Direction_same", "instances": 1094, "metric_value": 0.4131, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Bar", "instances": 641, "metric_value": 0.4335, "depth": 8}
								if obj[5]>0.0:
									# {"feature": "Education", "instances": 430, "metric_value": 0.4535, "depth": 9}
									if obj[3]<=4:
										# {"feature": "Restaurant20to50", "instances": 424, "metric_value": 0.4581, "depth": 10}
										if obj[7]>-1.0:
											return 'True'
										elif obj[7]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[3]>4:
										return 'True'
									else: return 'True'
								elif obj[5]<=0.0:
									# {"feature": "Education", "instances": 211, "metric_value": 0.3823, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Restaurant20to50", "instances": 156, "metric_value": 0.3592, "depth": 10}
										if obj[7]<=1.0:
											return 'True'
										elif obj[7]>1.0:
											return 'True'
										else: return 'True'
									elif obj[3]>2:
										# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.4159, "depth": 10}
										if obj[7]<=1.0:
											return 'True'
										elif obj[7]>1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]>0:
								# {"feature": "Education", "instances": 453, "metric_value": 0.3769, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Restaurant20to50", "instances": 328, "metric_value": 0.3568, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Bar", "instances": 286, "metric_value": 0.3728, "depth": 10}
										if obj[5]>-1.0:
											return 'True'
										elif obj[5]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Bar", "instances": 42, "metric_value": 0.2367, "depth": 10}
										if obj[5]>0.0:
											return 'True'
										elif obj[5]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Bar", "instances": 125, "metric_value": 0.4167, "depth": 9}
									if obj[5]<=3.0:
										# {"feature": "Restaurant20to50", "instances": 122, "metric_value": 0.414, "depth": 10}
										if obj[7]<=1.0:
											return 'True'
										elif obj[7]>1.0:
											return 'True'
										else: return 'True'
									elif obj[5]>3.0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[7]>3.0:
											return 'True'
										elif obj[7]<=3.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Direction_same", "instances": 445, "metric_value": 0.45, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Education", "instances": 340, "metric_value": 0.4342, "depth": 8}
								if obj[3]>0:
									# {"feature": "Bar", "instances": 233, "metric_value": 0.4534, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Restaurant20to50", "instances": 151, "metric_value": 0.4367, "depth": 10}
										if obj[7]>-1.0:
											return 'True'
										elif obj[7]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0.0:
										# {"feature": "Restaurant20to50", "instances": 82, "metric_value": 0.4631, "depth": 10}
										if obj[7]<=2.0:
											return 'True'
										elif obj[7]>2.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Bar", "instances": 107, "metric_value": 0.3784, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Restaurant20to50", "instances": 95, "metric_value": 0.4018, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.1111, "depth": 10}
										if obj[7]<=1.0:
											return 'True'
										elif obj[7]>1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]>0:
								# {"feature": "Bar", "instances": 105, "metric_value": 0.4799, "depth": 8}
								if obj[5]<=2.0:
									# {"feature": "Education", "instances": 88, "metric_value": 0.47, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.4403, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.4948, "depth": 10}
										if obj[7]<=2.0:
											return 'True'
										elif obj[7]>2.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[5]>2.0:
									# {"feature": "Education", "instances": 17, "metric_value": 0.4189, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4545, "depth": 10}
										if obj[7]<=2.0:
											return 'False'
										elif obj[7]>2.0:
											return 'True'
										else: return 'True'
									elif obj[3]>2:
										# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.1667, "depth": 10}
										if obj[7]>1.0:
											return 'False'
										elif obj[7]<=1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[4]>18.149362003525606:
						# {"feature": "Time", "instances": 118, "metric_value": 0.2949, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Bar", "instances": 71, "metric_value": 0.3405, "depth": 7}
							if obj[5]>1.0:
								# {"feature": "Direction_same", "instances": 41, "metric_value": 0.23, "depth": 8}
								if obj[8]>0:
									# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.317, "depth": 9}
									if obj[7]>1.0:
										# {"feature": "Education", "instances": 17, "metric_value": 0.4118, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=1.0:
										# {"feature": "Education", "instances": 11, "metric_value": 0.1455, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 30, "metric_value": 0.3911, "depth": 8}
								if obj[8]>0:
									# {"feature": "Education", "instances": 16, "metric_value": 0.2344, "depth": 9}
									if obj[3]>2:
										# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.4375, "depth": 10}
										if obj[7]<=1.0:
											return 'True'
										elif obj[7]>1.0:
											return 'False'
										else: return 'False'
									elif obj[3]<=2:
										return 'True'
									else: return 'True'
								elif obj[8]<=0:
									# {"feature": "Education", "instances": 14, "metric_value": 0.4571, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[7]<=1.0:
											return 'False'
										elif obj[7]>1.0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[7]<=1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[1]>1:
							# {"feature": "Bar", "instances": 47, "metric_value": 0.1789, "depth": 7}
							if obj[5]<=2.0:
								# {"feature": "Direction_same", "instances": 40, "metric_value": 0.1152, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Education", "instances": 34, "metric_value": 0.0539, "depth": 9}
									if obj[3]<=2:
										return 'True'
									elif obj[3]>2:
										# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.1333, "depth": 10}
										if obj[7]>1.0:
											return 'True'
										elif obj[7]<=1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>0:
									# {"feature": "Education", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[7]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[5]>2.0:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2857, "depth": 8}
								if obj[7]>1.0:
									# {"feature": "Education", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								elif obj[7]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Bar", "instances": 902, "metric_value": 0.349, "depth": 5}
					if obj[5]<=3.0:
						# {"feature": "Education", "instances": 848, "metric_value": 0.3366, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Time", "instances": 804, "metric_value": 0.3474, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Occupation", "instances": 489, "metric_value": 0.3124, "depth": 8}
								if obj[4]>2.5454774682183086:
									# {"feature": "Restaurant20to50", "instances": 406, "metric_value": 0.334, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 370, "metric_value": 0.3232, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 36, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=2.5454774682183086:
									# {"feature": "Restaurant20to50", "instances": 83, "metric_value": 0.1922, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 79, "metric_value": 0.2019, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Restaurant20to50", "instances": 315, "metric_value": 0.3935, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Occupation", "instances": 185, "metric_value": 0.4203, "depth": 9}
									if obj[4]<=7.243243243243243:
										# {"feature": "Direction_same", "instances": 124, "metric_value": 0.453, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[4]>7.243243243243243:
										# {"feature": "Direction_same", "instances": 61, "metric_value": 0.3537, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									# {"feature": "Occupation", "instances": 130, "metric_value": 0.3436, "depth": 9}
									if obj[4]<=19:
										# {"feature": "Direction_same", "instances": 122, "metric_value": 0.3354, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[4]>19:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>3:
							# {"feature": "Time", "instances": 44, "metric_value": 0.0744, "depth": 7}
							if obj[1]<=3:
								return 'True'
							elif obj[1]>3:
								# {"feature": "Occupation", "instances": 11, "metric_value": 0.2424, "depth": 8}
								if obj[4]<=7:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[4]>7:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[5]>3.0:
						# {"feature": "Time", "instances": 54, "metric_value": 0.4364, "depth": 6}
						if obj[1]>0:
							# {"feature": "Occupation", "instances": 44, "metric_value": 0.4408, "depth": 7}
							if obj[4]>1:
								# {"feature": "Education", "instances": 33, "metric_value": 0.3896, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.4365, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4012, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>3:
									return 'True'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Education", "instances": 11, "metric_value": 0.4959, "depth": 8}
								if obj[3]<=4:
									# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4959, "depth": 9}
									if obj[7]<=4.0:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]<=0:
							# {"feature": "Education", "instances": 10, "metric_value": 0.2667, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.2222, "depth": 8}
								if obj[7]<=1.0:
									return 'False'
								elif obj[7]>1.0:
									# {"feature": "Occupation", "instances": 3, "metric_value": 0.0, "depth": 9}
									if obj[4]<=7:
										return 'True'
									elif obj[4]>7:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[3]>2:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[9]>2:
				# {"feature": "Passanger", "instances": 271, "metric_value": 0.488, "depth": 4}
				if obj[0]>0:
					# {"feature": "Occupation", "instances": 261, "metric_value": 0.4886, "depth": 5}
					if obj[4]<=17.738927356162908:
						# {"feature": "Bar", "instances": 241, "metric_value": 0.4894, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Education", "instances": 163, "metric_value": 0.4783, "depth": 7}
							if obj[3]>0:
								# {"feature": "Time", "instances": 127, "metric_value": 0.4685, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Restaurant20to50", "instances": 105, "metric_value": 0.4444, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 90, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>2.0:
										# {"feature": "Direction_same", "instances": 15, "metric_value": 0.2311, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>1:
									# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.4471, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4844, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>2.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.4746, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Time", "instances": 31, "metric_value": 0.4785, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 27, "metric_value": 0.4938, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>2.0:
									# {"feature": "Time", "instances": 5, "metric_value": 0.3, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]<=0.0:
							# {"feature": "Time", "instances": 78, "metric_value": 0.4779, "depth": 7}
							if obj[1]>0:
								# {"feature": "Education", "instances": 69, "metric_value": 0.4666, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Restaurant20to50", "instances": 62, "metric_value": 0.4871, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 40, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 22, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>3:
									# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2143, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.381, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Education", "instances": 7, "metric_value": 0.4048, "depth": 9}
									if obj[3]>0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>17.738927356162908:
						# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.2637, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Bar", "instances": 13, "metric_value": 0.1282, "depth": 7}
							if obj[5]>0.0:
								return 'True'
							elif obj[5]<=0.0:
								# {"feature": "Education", "instances": 6, "metric_value": 0.2222, "depth": 8}
								if obj[3]>2:
									return 'True'
								elif obj[3]<=2:
									# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>1.0:
							# {"feature": "Education", "instances": 7, "metric_value": 0.3429, "depth": 7}
							if obj[3]>1:
								# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 8}
								if obj[1]>1:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[5]>1.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[5]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[1]<=1:
									return 'True'
								else: return 'True'
							elif obj[3]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]<=0:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.1, "depth": 5}
					if obj[7]<=2.0:
						return 'True'
					elif obj[7]>2.0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 6}
						if obj[4]>1:
							return 'True'
						elif obj[4]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2260, "metric_value": 0.4558, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Occupation", "instances": 1577, "metric_value": 0.4395, "depth": 3}
			if obj[4]>1.8509661496426837:
				# {"feature": "Education", "instances": 1312, "metric_value": 0.4571, "depth": 4}
				if obj[3]>0:
					# {"feature": "Coffeehouse", "instances": 846, "metric_value": 0.4314, "depth": 5}
					if obj[6]<=3.0:
						# {"feature": "Restaurant20to50", "instances": 795, "metric_value": 0.441, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Passanger", "instances": 570, "metric_value": 0.4164, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Time", "instances": 490, "metric_value": 0.3949, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Distance", "instances": 330, "metric_value": 0.4363, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 242, "metric_value": 0.4626, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 88, "metric_value": 0.3634, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Distance", "instances": 160, "metric_value": 0.2958, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 87, "metric_value": 0.2694, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 73, "metric_value": 0.3265, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>2:
								# {"feature": "Time", "instances": 80, "metric_value": 0.4795, "depth": 8}
								if obj[1]>0:
									# {"feature": "Distance", "instances": 78, "metric_value": 0.49, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 64, "metric_value": 0.4878, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 14, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[7]>1.0:
							# {"feature": "Distance", "instances": 225, "metric_value": 0.4824, "depth": 7}
							if obj[9]<=2:
								# {"feature": "Time", "instances": 187, "metric_value": 0.4894, "depth": 8}
								if obj[1]>0:
									# {"feature": "Passanger", "instances": 133, "metric_value": 0.4829, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Direction_same", "instances": 97, "metric_value": 0.4741, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[0]>2:
										# {"feature": "Direction_same", "instances": 36, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Passanger", "instances": 54, "metric_value": 0.4753, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 41, "metric_value": 0.4691, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[0]>1:
										# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4256, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[9]>2:
								# {"feature": "Passanger", "instances": 38, "metric_value": 0.3841, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 37, "metric_value": 0.3942, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 29, "metric_value": 0.3995, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[6]>3.0:
						# {"feature": "Distance", "instances": 51, "metric_value": 0.1696, "depth": 6}
						if obj[9]<=2:
							# {"feature": "Time", "instances": 37, "metric_value": 0.2194, "depth": 7}
							if obj[1]>2:
								# {"feature": "Passanger", "instances": 19, "metric_value": 0.0936, "depth": 8}
								if obj[0]>1:
									return 'False'
								elif obj[0]<=1:
									# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.1778, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]<=2:
								# {"feature": "Passanger", "instances": 18, "metric_value": 0.3264, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.2625, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.419, "depth": 10}
										if obj[8]>0:
											return 'False'
										elif obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>1.0:
										return 'False'
									else: return 'False'
								elif obj[0]>2:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[7]>2.0:
										return 'True'
									elif obj[7]<=2.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[9]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]<=0:
					# {"feature": "Restaurant20to50", "instances": 466, "metric_value": 0.487, "depth": 5}
					if obj[7]<=2.0:
						# {"feature": "Passanger", "instances": 441, "metric_value": 0.4848, "depth": 6}
						if obj[0]>0:
							# {"feature": "Time", "instances": 370, "metric_value": 0.4758, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Coffeehouse", "instances": 309, "metric_value": 0.4883, "depth": 8}
								if obj[6]<=3.0:
									# {"feature": "Distance", "instances": 279, "metric_value": 0.488, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 211, "metric_value": 0.4974, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 68, "metric_value": 0.4567, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]>3.0:
									# {"feature": "Distance", "instances": 30, "metric_value": 0.3889, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 24, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]>3:
								# {"feature": "Distance", "instances": 61, "metric_value": 0.3707, "depth": 8}
								if obj[9]<=1:
									# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.4448, "depth": 9}
									if obj[6]>0.0:
										# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4991, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[6]<=0.0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]>1:
									# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.2143, "depth": 9}
									if obj[6]<=1.0:
										# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[6]>1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]<=0:
							# {"feature": "Coffeehouse", "instances": 71, "metric_value": 0.4683, "depth": 7}
							if obj[6]>0.0:
								# {"feature": "Time", "instances": 52, "metric_value": 0.4587, "depth": 8}
								if obj[1]>2:
									# {"feature": "Distance", "instances": 33, "metric_value": 0.4843, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4994, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=2:
									# {"feature": "Distance", "instances": 19, "metric_value": 0.3709, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]<=0.0:
								# {"feature": "Time", "instances": 19, "metric_value": 0.3947, "depth": 8}
								if obj[1]>0:
									# {"feature": "Distance", "instances": 16, "metric_value": 0.4286, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4898, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[7]>2.0:
						# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.364, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Passanger", "instances": 20, "metric_value": 0.3077, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4256, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Time", "instances": 10, "metric_value": 0.4, "depth": 9}
									if obj[1]>1:
										# {"feature": "Distance", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[9]<=1:
											return 'True'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									elif obj[1]<=1:
										# {"feature": "Distance", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[9]<=3:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>0:
									# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[1]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=1:
											return 'True'
										else: return 'True'
									elif obj[1]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[6]>2.0:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.2, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 8}
								if obj[1]<=0:
									return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1.8509661496426837:
				# {"feature": "Restaurant20to50", "instances": 265, "metric_value": 0.3153, "depth": 4}
				if obj[7]>0.0:
					# {"feature": "Distance", "instances": 216, "metric_value": 0.3556, "depth": 5}
					if obj[9]<=2:
						# {"feature": "Coffeehouse", "instances": 177, "metric_value": 0.3768, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Education", "instances": 102, "metric_value": 0.3228, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Time", "instances": 86, "metric_value": 0.2967, "depth": 8}
								if obj[1]>1:
									# {"feature": "Direction_same", "instances": 52, "metric_value": 0.3429, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Passanger", "instances": 48, "metric_value": 0.3259, "depth": 10}
										if obj[0]>1:
											return 'False'
										elif obj[0]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[0]>1:
											return 'False'
										elif obj[0]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[1]<=1:
									# {"feature": "Passanger", "instances": 34, "metric_value": 0.2049, "depth": 9}
									if obj[0]>0:
										# {"feature": "Direction_same", "instances": 31, "metric_value": 0.22, "depth": 10}
										if obj[8]>0:
											return 'False'
										elif obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>2:
								# {"feature": "Time", "instances": 16, "metric_value": 0.3545, "depth": 8}
								if obj[1]>0:
									# {"feature": "Passanger", "instances": 11, "metric_value": 0.1636, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.175, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[0]>2:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[8]>0:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[0]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[6]>1.0:
							# {"feature": "Education", "instances": 75, "metric_value": 0.3927, "depth": 7}
							if obj[3]>0:
								# {"feature": "Passanger", "instances": 55, "metric_value": 0.3521, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 33, "metric_value": 0.2873, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Direction_same", "instances": 27, "metric_value": 0.2519, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[1]>3:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[0]>1:
									# {"feature": "Time", "instances": 22, "metric_value": 0.4167, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4688, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.1667, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]<=0:
								# {"feature": "Passanger", "instances": 20, "metric_value": 0.4125, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 12, "metric_value": 0.3125, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.1875, "depth": 10}
										if obj[8]>0:
											return 'True'
										elif obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]>1:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[0]>1:
									# {"feature": "Time", "instances": 8, "metric_value": 0.4286, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[9]>2:
						# {"feature": "Passanger", "instances": 39, "metric_value": 0.1835, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coffeehouse", "instances": 38, "metric_value": 0.1655, "depth": 7}
							if obj[6]>0.0:
								# {"feature": "Education", "instances": 27, "metric_value": 0.0684, "depth": 8}
								if obj[3]<=1:
									return 'False'
								elif obj[3]>1:
									# {"feature": "Time", "instances": 13, "metric_value": 0.1399, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1653, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=0.0:
								# {"feature": "Education", "instances": 11, "metric_value": 0.3737, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Time", "instances": 9, "metric_value": 0.3333, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]<=0.0:
					# {"feature": "Education", "instances": 49, "metric_value": 0.049, "depth": 5}
					if obj[3]<=4:
						return 'False'
					elif obj[3]>4:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.2667, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 7}
							if obj[1]>0:
								# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=1:
											return 'False'
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
		elif obj[5]>1.0:
			# {"feature": "Restaurant20to50", "instances": 683, "metric_value": 0.4668, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Passanger", "instances": 562, "metric_value": 0.4802, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Time", "instances": 474, "metric_value": 0.486, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Occupation", "instances": 308, "metric_value": 0.4768, "depth": 6}
						if obj[4]>0:
							# {"feature": "Direction_same", "instances": 304, "metric_value": 0.4789, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Distance", "instances": 215, "metric_value": 0.482, "depth": 8}
								if obj[9]>1:
									# {"feature": "Education", "instances": 206, "metric_value": 0.4862, "depth": 9}
									if obj[3]<=4:
										# {"feature": "Coffeehouse", "instances": 205, "metric_value": 0.4876, "depth": 10}
										if obj[6]>1.0:
											return 'True'
										elif obj[6]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[3]>4:
										return 'True'
									else: return 'True'
								elif obj[9]<=1:
									# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.1481, "depth": 9}
									if obj[6]<=3.0:
										return 'False'
									elif obj[6]>3.0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[8]>0:
								# {"feature": "Coffeehouse", "instances": 89, "metric_value": 0.4305, "depth": 8}
								if obj[6]<=3.0:
									# {"feature": "Education", "instances": 81, "metric_value": 0.4194, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Distance", "instances": 78, "metric_value": 0.4355, "depth": 10}
										if obj[9]<=1:
											return 'True'
										elif obj[9]>1:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										return 'True'
									else: return 'True'
								elif obj[6]>3.0:
									# {"feature": "Education", "instances": 8, "metric_value": 0.3, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Distance", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[9]<=1:
											return 'True'
										else: return 'True'
									elif obj[3]>2:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						# {"feature": "Occupation", "instances": 166, "metric_value": 0.4852, "depth": 6}
						if obj[4]<=8.74698795180723:
							# {"feature": "Coffeehouse", "instances": 97, "metric_value": 0.4678, "depth": 7}
							if obj[6]>1.0:
								# {"feature": "Education", "instances": 61, "metric_value": 0.4869, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Distance", "instances": 60, "metric_value": 0.4936, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 57, "metric_value": 0.496, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>3:
									return 'False'
								else: return 'False'
							elif obj[6]<=1.0:
								# {"feature": "Education", "instances": 36, "metric_value": 0.3838, "depth": 8}
								if obj[3]>0:
									# {"feature": "Distance", "instances": 25, "metric_value": 0.4667, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4848, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									# {"feature": "Distance", "instances": 11, "metric_value": 0.1515, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>8.74698795180723:
							# {"feature": "Distance", "instances": 69, "metric_value": 0.4763, "depth": 7}
							if obj[9]<=1:
								# {"feature": "Education", "instances": 44, "metric_value": 0.4649, "depth": 8}
								if obj[3]<=1:
									# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.3961, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3367, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[6]>2.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>1:
									# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.4257, "depth": 9}
									if obj[6]>1.0:
										# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4567, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[6]<=1.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[9]>1:
								# {"feature": "Education", "instances": 25, "metric_value": 0.4456, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4678, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.4815, "depth": 10}
										if obj[6]>1.0:
											return 'True'
										elif obj[6]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[6]>3.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[6]<=3.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 88, "metric_value": 0.3215, "depth": 5}
					if obj[1]>2:
						# {"feature": "Education", "instances": 67, "metric_value": 0.259, "depth": 6}
						if obj[3]>1:
							# {"feature": "Occupation", "instances": 37, "metric_value": 0.3524, "depth": 7}
							if obj[4]>4:
								# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.2816, "depth": 8}
								if obj[6]<=3.0:
									# {"feature": "Distance", "instances": 21, "metric_value": 0.3079, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 15, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>3.0:
									return 'True'
								else: return 'True'
							elif obj[4]<=4:
								# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.3155, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Distance", "instances": 8, "metric_value": 0.2143, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										return 'True'
									else: return 'True'
								elif obj[6]>1.0:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.4167, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[3]<=1:
							# {"feature": "Occupation", "instances": 30, "metric_value": 0.1185, "depth": 7}
							if obj[4]>6:
								# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.188, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.2521, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>2.0:
									return 'True'
								else: return 'True'
							elif obj[4]<=6:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=2:
						# {"feature": "Occupation", "instances": 21, "metric_value": 0.3079, "depth": 6}
						if obj[4]<=12:
							# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.28, "depth": 7}
							if obj[6]>0.0:
								# {"feature": "Education", "instances": 10, "metric_value": 0.375, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 8, "metric_value": 0.4688, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>2:
									return 'False'
								else: return 'False'
							elif obj[6]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[4]>12:
							# {"feature": "Education", "instances": 6, "metric_value": 0.2222, "depth": 7}
							if obj[3]>1:
								# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.3333, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[3]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[7]>2.0:
				# {"feature": "Occupation", "instances": 121, "metric_value": 0.3469, "depth": 4}
				if obj[4]<=9:
					# {"feature": "Education", "instances": 77, "metric_value": 0.2552, "depth": 5}
					if obj[3]>0:
						# {"feature": "Time", "instances": 69, "metric_value": 0.2157, "depth": 6}
						if obj[1]>0:
							# {"feature": "Direction_same", "instances": 52, "metric_value": 0.2684, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Coffeehouse", "instances": 48, "metric_value": 0.2406, "depth": 8}
								if obj[6]>1.0:
									# {"feature": "Passanger", "instances": 40, "metric_value": 0.2819, "depth": 9}
									if obj[0]>0:
										# {"feature": "Distance", "instances": 36, "metric_value": 0.3115, "depth": 10}
										if obj[9]>1:
											return 'True'
										elif obj[9]<=1:
											return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=1.0:
									return 'True'
								else: return 'True'
							elif obj[8]>0:
								# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.0, "depth": 8}
								if obj[6]>3.0:
									return 'False'
								elif obj[6]<=3.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.3333, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.0, "depth": 7}
							if obj[6]<=2.0:
								return 'True'
							elif obj[6]>2.0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>9:
					# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.4211, "depth": 5}
					if obj[6]<=3.0:
						# {"feature": "Passanger", "instances": 38, "metric_value": 0.463, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Time", "instances": 29, "metric_value": 0.4497, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Education", "instances": 19, "metric_value": 0.4173, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Distance", "instances": 12, "metric_value": 0.35, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4167, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[9]>2:
										return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Distance", "instances": 7, "metric_value": 0.4286, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]>2:
								# {"feature": "Direction_same", "instances": 10, "metric_value": 0.3111, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Distance", "instances": 9, "metric_value": 0.1944, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Education", "instances": 8, "metric_value": 0.1875, "depth": 10}
										if obj[3]>1:
											return 'False'
										elif obj[3]<=1:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										return 'True'
									else: return 'True'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[0]>2:
							# {"feature": "Education", "instances": 9, "metric_value": 0.2667, "depth": 7}
							if obj[3]>0:
								# {"feature": "Time", "instances": 5, "metric_value": 0.4667, "depth": 8}
								if obj[1]>2:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=2:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>3.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
