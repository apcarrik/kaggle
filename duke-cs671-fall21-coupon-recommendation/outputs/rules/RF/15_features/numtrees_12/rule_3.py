def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[11]>0.0:
		# {"feature": "Income", "instances": 65, "metric_value": 0.9612, "depth": 2}
		if obj[9]>1:
			# {"feature": "Education", "instances": 52, "metric_value": 0.8905, "depth": 3}
			if obj[7]<=2:
				# {"feature": "Time", "instances": 41, "metric_value": 0.8015, "depth": 4}
				if obj[1]>0:
					# {"feature": "Passanger", "instances": 30, "metric_value": 0.8813, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Age", "instances": 24, "metric_value": 0.9544, "depth": 6}
						if obj[5]>0:
							# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Occupation", "instances": 18, "metric_value": 0.8524, "depth": 8}
								if obj[8]<=10:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9403, "depth": 9}
									if obj[12]>0.0:
										# {"feature": "Gender", "instances": 13, "metric_value": 0.8905, "depth": 10}
										if obj[4]>0:
											# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[14]>1:
														# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[3]<=0:
															# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[14]<=1:
														return 'True'
													else: return 'True'
												elif obj[10]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[6]>0:
												# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													elif obj[10]>1.0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									elif obj[12]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[8]>10:
									return 'True'
								else: return 'True'
							elif obj[2]>3:
								# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]<=0:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[10]<=1.0:
										return 'True'
									elif obj[10]>1.0:
										return 'False'
									else: return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[7]>2:
				# {"feature": "Gender", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[4]>0:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=2:
						return 'False'
					elif obj[2]>2:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=1:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[2]>1:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[10]>0.0:
						return 'False'
					elif obj[10]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[11]<=0.0:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[7]>0:
					return 'True'
				elif obj[7]<=0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]>2:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=2:
							return 'True'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					elif obj[0]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[12]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
