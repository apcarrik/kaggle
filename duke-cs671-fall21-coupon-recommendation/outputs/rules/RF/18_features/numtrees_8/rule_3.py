def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9996, "depth": 1}
	if obj[3]>1:
		# {"feature": "Coupon_validity", "instances": 95, "metric_value": 0.9768, "depth": 2}
		if obj[4]>0:
			# {"feature": "Maritalstatus", "instances": 50, "metric_value": 0.971, "depth": 3}
			if obj[7]>0:
				# {"feature": "Income", "instances": 35, "metric_value": 0.8631, "depth": 4}
				if obj[11]>1:
					# {"feature": "Occupation", "instances": 28, "metric_value": 0.9403, "depth": 5}
					if obj[10]<=12:
						# {"feature": "Age", "instances": 24, "metric_value": 0.9799, "depth": 6}
						if obj[6]>0:
							# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.9183, "depth": 7}
							if obj[13]<=3.0:
								# {"feature": "Time", "instances": 17, "metric_value": 0.9774, "depth": 8}
								if obj[2]>0:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.8631, "depth": 9}
									if obj[15]<=1.0:
										# {"feature": "Weather", "instances": 10, "metric_value": 0.469, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=1:
												return 'False'
											elif obj[9]>1:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[15]>1.0:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[5]>0:
											# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[0]<=3:
												# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8]<=0:
														# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[12]<=0.0:
																# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14]<=3.0:
																	# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[16]<=0:
																		# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=2:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[2]<=0:
									return 'True'
								else: return 'True'
							elif obj[13]>3.0:
								return 'False'
							else: return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[10]>12:
						return 'False'
					else: return 'False'
				elif obj[11]<=1:
					return 'False'
				else: return 'False'
			elif obj[7]<=0:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[15]>1.0:
					# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[6]<=3:
						# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[14]<=2.0:
							# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[1]<=1:
								return 'True'
							elif obj[1]>1:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=0:
									return 'True'
								elif obj[5]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[14]>2.0:
							return 'False'
						else: return 'False'
					elif obj[6]>3:
						return 'False'
					else: return 'False'
				elif obj[15]<=1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=0:
			# {"feature": "Distance", "instances": 45, "metric_value": 0.7219, "depth": 3}
			if obj[17]>1:
				# {"feature": "Bar", "instances": 27, "metric_value": 0.3809, "depth": 4}
				if obj[12]<=1.0:
					return 'True'
				elif obj[12]>1.0:
					# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[7]>0:
						return 'True'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[17]<=1:
				# {"feature": "Time", "instances": 18, "metric_value": 0.9641, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[6]>3:
						return 'True'
					elif obj[6]<=3:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=0:
								return 'False'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[2]>2:
					# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[6]<=6:
						return 'False'
					elif obj[6]>6:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Bar", "instances": 32, "metric_value": 0.8571, "depth": 2}
		if obj[12]<=3.0:
			# {"feature": "Distance", "instances": 30, "metric_value": 0.7838, "depth": 3}
			if obj[17]<=2:
				# {"feature": "Direction_same", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[16]<=0:
					# {"feature": "Income", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[11]<=4:
						# {"feature": "Age", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[6]<=4:
							# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[10]<=5:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[15]>1.0:
									return 'False'
								elif obj[15]<=1.0:
									return 'True'
								else: return 'True'
							elif obj[10]>5:
								return 'True'
							else: return 'True'
						elif obj[6]>4:
							return 'False'
						else: return 'False'
					elif obj[11]>4:
						# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[7]<=1:
							return 'False'
						elif obj[7]>1:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[16]>0:
					return 'False'
				else: return 'False'
			elif obj[17]>2:
				return 'False'
			else: return 'False'
		elif obj[12]>3.0:
			return 'True'
		else: return 'True'
	else: return 'False'
