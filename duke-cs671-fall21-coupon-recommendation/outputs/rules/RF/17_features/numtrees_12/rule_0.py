def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon_validity", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[4]<=0:
		# {"feature": "Coupon", "instances": 48, "metric_value": 0.9544, "depth": 2}
		if obj[3]>1:
			# {"feature": "Income", "instances": 34, "metric_value": 0.8338, "depth": 3}
			if obj[11]<=7:
				# {"feature": "Weather", "instances": 32, "metric_value": 0.7579, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Time", "instances": 26, "metric_value": 0.8404, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9183, "depth": 6}
						if obj[14]<=2.0:
							# {"feature": "Children", "instances": 20, "metric_value": 0.8813, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Age", "instances": 13, "metric_value": 0.8905, "depth": 9}
									if obj[6]<=4:
										# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[10]<=9:
											# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 11}
											if obj[13]<=1.0:
												# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[7]<=1:
														# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[12]<=2.0:
															return 'True'
														elif obj[12]>2.0:
															# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[15]<=0:
																return 'True'
															elif obj[15]>0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[7]>1:
														return 'False'
													else: return 'False'
												elif obj[0]>1:
													return 'False'
												else: return 'False'
											elif obj[13]>1.0:
												return 'True'
											else: return 'True'
										elif obj[10]>9:
											return 'False'
										else: return 'False'
									elif obj[6]>4:
										return 'True'
									else: return 'True'
								elif obj[9]>2:
									return 'False'
								else: return 'False'
							elif obj[8]>0:
								return 'True'
							else: return 'True'
						elif obj[14]>2.0:
							return 'False'
						else: return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[11]>7:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			# {"feature": "Bar", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[12]<=0.0:
				return 'False'
			elif obj[12]>0.0:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[9]<=2:
					return 'True'
				elif obj[9]>2:
					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>0:
		# {"feature": "Occupation", "instances": 37, "metric_value": 0.9353, "depth": 2}
		if obj[10]<=6:
			# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[13]<=3.0:
				# {"feature": "Time", "instances": 18, "metric_value": 0.9641, "depth": 4}
				if obj[2]>1:
					# {"feature": "Age", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[6]<=4:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[8]>0:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[12]<=1.0:
									return 'False'
								elif obj[12]>1.0:
									return 'True'
								else: return 'True'
							elif obj[8]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							return 'False'
						else: return 'False'
					elif obj[6]>4:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>2:
							return 'True'
						elif obj[3]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[13]>3.0:
				return 'False'
			else: return 'False'
		elif obj[10]>6:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.5226, "depth": 3}
			if obj[14]>0.0:
				# {"feature": "Coupon", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=0:
						return 'False'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[14]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
