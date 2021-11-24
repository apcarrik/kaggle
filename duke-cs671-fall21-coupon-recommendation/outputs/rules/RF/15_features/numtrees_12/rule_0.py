def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[14]<=2:
		# {"feature": "Occupation", "instances": 72, "metric_value": 0.9316, "depth": 2}
		if obj[8]>1:
			# {"feature": "Age", "instances": 61, "metric_value": 0.967, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Time", "instances": 33, "metric_value": 0.8454, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 26, "metric_value": 0.9306, "depth": 5}
					if obj[7]<=3:
						# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.9544, "depth": 6}
						if obj[12]<=2.0:
							# {"feature": "Income", "instances": 23, "metric_value": 0.9321, "depth": 7}
							if obj[9]>1:
								# {"feature": "Coupon", "instances": 21, "metric_value": 0.9587, "depth": 8}
								if obj[2]>1:
									# {"feature": "Children", "instances": 12, "metric_value": 0.8113, "depth": 9}
									if obj[6]>0:
										return 'True'
									elif obj[6]<=0:
										# {"feature": "Coupon_validity", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[3]>0:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=1.0:
													return 'True'
												elif obj[10]>1.0:
													return 'False'
												else: return 'False'
											elif obj[0]>1:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[2]<=1:
									# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[11]<=1.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[4]>0:
											return 'False'
										elif obj[4]<=0:
											# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[11]>1.0:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[0]>0:
											return 'True'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[9]<=1:
								return 'True'
							else: return 'True'
						elif obj[12]>2.0:
							return 'False'
						else: return 'False'
					elif obj[7]>3:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[5]>2:
				# {"feature": "Time", "instances": 28, "metric_value": 0.9963, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Coupon", "instances": 18, "metric_value": 0.9641, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Income", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[9]<=4:
							# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[10]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[12]>0.0:
									# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]>0:
											return 'True'
										elif obj[7]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[12]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[10]>1.0:
								return 'True'
							else: return 'True'
						elif obj[9]>4:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[9]<=7:
							return 'False'
						elif obj[9]>7:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>2:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[2]>0:
						# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[11]>-1.0:
							return 'False'
						elif obj[11]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[8]<=1:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[11]<=2.0:
				return 'True'
			elif obj[11]>2.0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[14]>2:
		# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[12]<=1.0:
			return 'False'
		elif obj[12]>1.0:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=4:
					return 'False'
				elif obj[5]>4:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
