def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9719, "depth": 1}
	if obj[4]>1:
		# {"feature": "Coupon_validity", "instances": 92, "metric_value": 0.8991, "depth": 2}
		if obj[5]>0:
			# {"feature": "Weather", "instances": 47, "metric_value": 0.9971, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Restaurantlessthan20", "instances": 42, "metric_value": 0.9737, "depth": 4}
				if obj[15]<=3.0:
					# {"feature": "Occupation", "instances": 38, "metric_value": 0.9268, "depth": 5}
					if obj[11]<=9:
						# {"feature": "Time", "instances": 24, "metric_value": 0.7383, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9183, "depth": 7}
							if obj[16]<=1.0:
								# {"feature": "Income", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[12]>4:
									# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]>1:
										return 'False'
									elif obj[7]<=1:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=1:
											return 'True'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[12]<=4:
									# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6]<=0:
										return 'True'
									elif obj[6]>0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[16]>1.0:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							return 'True'
						else: return 'True'
					elif obj[11]>9:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[13]>1.0:
							# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[14]<=1.0:
								return 'False'
							elif obj[14]>1.0:
								# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[12]<=2:
									return 'True'
								elif obj[12]>2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[13]<=1.0:
							# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[2]>55:
								return 'True'
							elif obj[2]<=55:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[15]>3.0:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		elif obj[5]<=0:
			# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.6236, "depth": 3}
			if obj[16]>-1.0:
				# {"feature": "Occupation", "instances": 44, "metric_value": 0.5746, "depth": 4}
				if obj[11]<=14:
					# {"feature": "Coffeehouse", "instances": 40, "metric_value": 0.469, "depth": 5}
					if obj[14]<=1.0:
						# {"feature": "Time", "instances": 23, "metric_value": 0.6666, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Direction_same", "instances": 16, "metric_value": 0.8113, "depth": 7}
							if obj[17]<=0:
								# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[7]>1:
									# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[10]<=2:
										return 'True'
									elif obj[10]>2:
										return 'False'
									else: return 'False'
								elif obj[7]<=1:
									# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[13]<=2.0:
										return 'False'
									elif obj[13]>2.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[17]>0:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							return 'True'
						else: return 'True'
					elif obj[14]>1.0:
						return 'True'
					else: return 'True'
				elif obj[11]>14:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							return 'True'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[16]<=-1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]<=1:
		# {"feature": "Bar", "instances": 35, "metric_value": 0.9518, "depth": 2}
		if obj[13]<=2.0:
			# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.9183, "depth": 3}
			if obj[14]<=3.0:
				# {"feature": "Income", "instances": 29, "metric_value": 0.9576, "depth": 4}
				if obj[12]<=7:
					# {"feature": "Age", "instances": 26, "metric_value": 0.9829, "depth": 5}
					if obj[7]<=6:
						# {"feature": "Occupation", "instances": 24, "metric_value": 0.995, "depth": 6}
						if obj[11]>1:
							# {"feature": "Education", "instances": 22, "metric_value": 0.976, "depth": 7}
							if obj[10]>1:
								# {"feature": "Restaurantlessthan20", "instances": 16, "metric_value": 0.896, "depth": 8}
								if obj[15]<=2.0:
									# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[0]>0:
										# {"feature": "Weather", "instances": 10, "metric_value": 1.0, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Temperature", "instances": 9, "metric_value": 0.9911, "depth": 11}
											if obj[2]<=55:
												# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[16]>0.0:
													# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[3]>0:
														# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[5]>0:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[6]<=0:
																# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=1:
																		# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=0:
																			# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]<=2:
																				return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[5]<=0:
															return 'False'
														else: return 'False'
													elif obj[3]<=0:
														# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[6]<=0:
															# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[8]>0:
																return 'False'
															elif obj[8]<=0:
																return 'True'
															else: return 'True'
														elif obj[6]>0:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[16]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[2]>55:
												return 'True'
											else: return 'True'
										elif obj[1]>1:
											return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								elif obj[15]>2.0:
									return 'False'
								else: return 'False'
							elif obj[10]<=1:
								# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=1:
										return 'False'
									elif obj[8]>1:
										return 'True'
									else: return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[11]<=1:
							return 'True'
						else: return 'True'
					elif obj[7]>6:
						return 'False'
					else: return 'False'
				elif obj[12]>7:
					return 'False'
				else: return 'False'
			elif obj[14]>3.0:
				return 'False'
			else: return 'False'
		elif obj[13]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
