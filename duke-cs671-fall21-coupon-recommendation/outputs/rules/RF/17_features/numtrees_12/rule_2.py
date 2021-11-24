def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.9259, "depth": 1}
	if obj[13]>0.0:
		# {"feature": "Occupation", "instances": 72, "metric_value": 0.8524, "depth": 2}
		if obj[10]>1:
			# {"feature": "Coupon", "instances": 62, "metric_value": 0.9072, "depth": 3}
			if obj[3]>0:
				# {"feature": "Passanger", "instances": 51, "metric_value": 0.819, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Income", "instances": 30, "metric_value": 0.9481, "depth": 5}
					if obj[11]<=6:
						# {"feature": "Maritalstatus", "instances": 28, "metric_value": 0.9059, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.9427, "depth": 7}
							if obj[14]>-1.0:
								# {"feature": "Coupon_validity", "instances": 24, "metric_value": 0.9183, "depth": 8}
								if obj[4]>0:
									# {"feature": "Weather", "instances": 14, "metric_value": 0.9852, "depth": 9}
									if obj[1]<=0:
										# {"feature": "Time", "instances": 12, "metric_value": 0.9183, "depth": 10}
										if obj[2]<=3:
											# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 11}
											if obj[16]<=2:
												# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 12}
												if obj[6]<=4:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[5]>0:
														# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[8]<=0:
															return 'True'
														elif obj[8]>0:
															# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9]>0:
																return 'True'
															elif obj[9]<=0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]>4:
													return 'True'
												else: return 'True'
											elif obj[16]>2:
												return 'False'
											else: return 'False'
										elif obj[2]>3:
											return 'False'
										else: return 'False'
									elif obj[1]>0:
										return 'False'
									else: return 'False'
								elif obj[4]<=0:
									# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[12]<=2.0:
										# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[9]<=3:
											return 'True'
										elif obj[9]>3:
											# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1]>0:
												return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[12]>2.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[14]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[7]>2:
							return 'True'
						else: return 'True'
					elif obj[11]>6:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.4537, "depth": 5}
					if obj[14]<=1.0:
						return 'True'
					elif obj[14]>1.0:
						# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[3]<=0:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[12]>1.0:
					# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[12]<=1.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[10]<=1:
			return 'True'
		else: return 'True'
	elif obj[13]<=0.0:
		# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[0]>0:
			# {"feature": "Coupon_validity", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=0:
					return 'True'
				elif obj[8]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
