def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 1.0, "depth": 1}
	if obj[16]<=2:
		# {"feature": "Coffeehouse", "instances": 105, "metric_value": 0.981, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Income", "instances": 78, "metric_value": 0.9049, "depth": 3}
			if obj[11]>3:
				# {"feature": "Coupon", "instances": 42, "metric_value": 0.7025, "depth": 4}
				if obj[3]>1:
					# {"feature": "Time", "instances": 33, "metric_value": 0.5328, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						# {"feature": "Passanger", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[7]<=1:
								# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[6]>4:
									# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[8]<=0:
										return 'False'
									elif obj[8]>0:
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=0:
											return 'False'
										elif obj[9]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[6]<=4:
									# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[8]<=0:
										return 'True'
									elif obj[8]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]>1:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=1:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[9]<=1:
						# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=3:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=3:
								return 'True'
							elif obj[2]>3:
								return 'False'
							else: return 'False'
						elif obj[6]>3:
							return 'False'
						else: return 'False'
					elif obj[9]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[11]<=3:
				# {"feature": "Maritalstatus", "instances": 36, "metric_value": 0.9978, "depth": 4}
				if obj[7]>0:
					# {"feature": "Time", "instances": 20, "metric_value": 0.8813, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[10]<=10:
							# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=4:
								return 'False'
							elif obj[6]>4:
								# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]>3:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=0:
											# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8]<=1:
														# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[12]<=0.0:
																# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14]<=2.0:
																	# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]<=3:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[10]>10:
							return 'True'
						else: return 'True'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				elif obj[7]<=0:
					# {"feature": "Education", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[9]>0:
						# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					elif obj[9]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[13]<=0.0:
			# {"feature": "Coupon", "instances": 27, "metric_value": 0.8767, "depth": 3}
			if obj[3]>3:
				# {"feature": "Income", "instances": 17, "metric_value": 0.3228, "depth": 4}
				if obj[11]<=6:
					return 'False'
				elif obj[11]>6:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>2:
						return 'False'
					elif obj[0]<=2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=3:
				# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[6]<=4:
					# {"feature": "Gender", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'False'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]>4:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[16]>2:
		# {"feature": "Coupon", "instances": 22, "metric_value": 0.4395, "depth": 2}
		if obj[3]<=2:
			return 'False'
		elif obj[3]>2:
			# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>1:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=1:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=2:
												# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=7:
													# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=2.0:
															# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=3.0:
																# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14]<=2.0:
																	# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'False'
