def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[10]>1:
		# {"feature": "Passanger", "instances": 80, "metric_value": 0.9778, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9183, "depth": 3}
			if obj[14]<=3.0:
				# {"feature": "Income", "instances": 49, "metric_value": 0.8886, "depth": 4}
				if obj[11]>1:
					# {"feature": "Coffeehouse", "instances": 38, "metric_value": 0.9495, "depth": 5}
					if obj[13]<=3.0:
						# {"feature": "Time", "instances": 34, "metric_value": 0.9774, "depth": 6}
						if obj[2]<=1:
							# {"feature": "Bar", "instances": 22, "metric_value": 0.9024, "depth": 7}
							if obj[12]>0.0:
								# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 8}
								if obj[3]>1:
									return 'False'
								elif obj[3]<=1:
									return 'True'
								else: return 'True'
							elif obj[12]<=0.0:
								# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[3]>1:
									# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[7]<=1:
										# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[1]<=0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[6]>1:
													return 'True'
												elif obj[6]<=1:
													# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[4]>0:
														return 'False'
													elif obj[4]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										elif obj[1]>0:
											return 'False'
										else: return 'False'
									elif obj[7]>1:
										return 'True'
									else: return 'True'
								elif obj[3]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[2]>1:
							# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[12]<=2.0:
								# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[3]<=1:
									# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[6]>0:
											# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[9]>0:
												# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7]>1:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[16]<=1:
														return 'True'
													elif obj[16]>1:
														return 'False'
													else: return 'False'
												elif obj[7]<=1:
													return 'True'
												else: return 'True'
											elif obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[6]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								elif obj[3]>1:
									return 'True'
								else: return 'True'
							elif obj[12]>2.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[13]>3.0:
						return 'False'
					else: return 'False'
				elif obj[11]<=1:
					# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>1:
							return 'False'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[14]>3.0:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Age", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[6]<=3:
				# {"feature": "Coupon", "instances": 20, "metric_value": 0.9928, "depth": 4}
				if obj[3]>1:
					# {"feature": "Distance", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[16]>1:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[12]<=1.0:
							# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[1]<=0:
								return 'False'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						elif obj[12]>1.0:
							return 'True'
						else: return 'True'
					elif obj[16]<=1:
						# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[13]<=2.0:
							return 'True'
						elif obj[13]>2.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[6]>3:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[3]<=1:
					# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[8]<=0:
						# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[11]>4:
								return 'False'
							elif obj[11]<=4:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[8]>0:
						return 'True'
					else: return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[10]<=1:
		return 'True'
	else: return 'True'
