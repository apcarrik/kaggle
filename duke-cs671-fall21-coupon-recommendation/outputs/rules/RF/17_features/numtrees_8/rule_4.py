def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.987, "depth": 1}
	if obj[3]>1:
		# {"feature": "Passanger", "instances": 92, "metric_value": 0.9416, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 88, "metric_value": 0.9145, "depth": 3}
			if obj[9]>1:
				# {"feature": "Income", "instances": 46, "metric_value": 0.9877, "depth": 4}
				if obj[11]<=5:
					# {"feature": "Occupation", "instances": 31, "metric_value": 0.8238, "depth": 5}
					if obj[10]<=9:
						# {"feature": "Maritalstatus", "instances": 22, "metric_value": 0.9457, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.8315, "depth": 7}
							if obj[13]<=1.0:
								# {"feature": "Direction_same", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[15]<=0:
									# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[12]>1.0:
										# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[6]>0:
											# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[2]>2:
												# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1]<=0:
													# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[4]<=1:
														# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[5]<=1:
															# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[8]<=1:
																# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14]<=2.0:
																	# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[16]<=2:
																		return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[2]<=2:
												return 'False'
											else: return 'False'
										elif obj[6]<=0:
											return 'True'
										else: return 'True'
									elif obj[12]<=1.0:
										return 'True'
									else: return 'True'
								elif obj[15]>0:
									return 'False'
								else: return 'False'
							elif obj[13]>1.0:
								return 'True'
							else: return 'True'
						elif obj[7]>2:
							return 'False'
						else: return 'False'
					elif obj[10]>9:
						return 'True'
					else: return 'True'
				elif obj[11]>5:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[10]<=10:
						return 'False'
					elif obj[10]>10:
						# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[16]<=1:
							# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						elif obj[16]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[9]<=1:
				# {"feature": "Direction_same", "instances": 42, "metric_value": 0.7496, "depth": 4}
				if obj[15]<=0:
					# {"feature": "Income", "instances": 31, "metric_value": 0.8691, "depth": 5}
					if obj[11]<=5:
						# {"feature": "Occupation", "instances": 22, "metric_value": 0.976, "depth": 6}
						if obj[10]>1:
							# {"feature": "Children", "instances": 17, "metric_value": 0.874, "depth": 7}
							if obj[8]>0:
								# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[14]>0.0:
									# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[4]>0:
										# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[12]<=2.0:
											return 'False'
										elif obj[12]>2.0:
											return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[14]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[8]<=0:
								return 'True'
							else: return 'True'
						elif obj[10]<=1:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[13]<=1.0:
								return 'False'
							elif obj[13]>1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[11]>5:
						return 'True'
					else: return 'True'
				elif obj[15]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[3]<=1:
		# {"feature": "Income", "instances": 35, "metric_value": 0.9518, "depth": 2}
		if obj[11]<=6:
			# {"feature": "Bar", "instances": 32, "metric_value": 0.9745, "depth": 3}
			if obj[12]<=3.0:
				# {"feature": "Age", "instances": 30, "metric_value": 0.9481, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[13]>0.0:
						# {"feature": "Coupon_validity", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=0:
							# {"feature": "Weather", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[2]<=2:
									# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[8]<=0:
										return 'True'
									elif obj[8]>0:
										# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[10]>5:
											return 'False'
										elif obj[10]<=5:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[2]>2:
									return 'False'
								else: return 'False'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					elif obj[13]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[6]>2:
					# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[10]<=7:
						# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[13]<=1.0:
							return 'True'
						elif obj[13]>1.0:
							# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]<=0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]>0:
									return 'True'
								elif obj[5]<=0:
									return 'False'
								else: return 'False'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[10]>7:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[12]>3.0:
				return 'True'
			else: return 'True'
		elif obj[11]>6:
			return 'False'
		else: return 'False'
	else: return 'False'
