def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Age", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[6]>1:
		# {"feature": "Direction_same", "instances": 51, "metric_value": 0.9975, "depth": 2}
		if obj[14]<=0:
			# {"feature": "Income", "instances": 45, "metric_value": 0.9968, "depth": 3}
			if obj[10]<=7:
				# {"feature": "Bar", "instances": 40, "metric_value": 0.9982, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.9629, "depth": 5}
					if obj[12]<=3.0:
						# {"feature": "Passanger", "instances": 27, "metric_value": 0.9911, "depth": 6}
						if obj[0]>0:
							# {"feature": "Coupon", "instances": 25, "metric_value": 0.971, "depth": 7}
							if obj[3]>0:
								# {"feature": "Occupation", "instances": 20, "metric_value": 1.0, "depth": 8}
								if obj[9]<=5:
									# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 9}
									if obj[2]<=1:
										# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[8]<=1:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[13]<=1.0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[15]>1:
													return 'False'
												elif obj[15]<=1:
													return 'True'
												else: return 'True'
											elif obj[13]>1.0:
												return 'True'
											else: return 'True'
										elif obj[8]>1:
											return 'True'
										else: return 'True'
									elif obj[2]>1:
										return 'True'
									else: return 'True'
								elif obj[9]>5:
									# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=2:
											return 'True'
										elif obj[8]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[12]>3.0:
						return 'False'
					else: return 'False'
				elif obj[11]>1.0:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[9]>4:
						return 'True'
					elif obj[9]<=4:
						# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[4]<=0:
							return 'True'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[10]>7:
				return 'True'
			else: return 'True'
		elif obj[14]>0:
			return 'False'
		else: return 'False'
	elif obj[6]<=1:
		# {"feature": "Gender", "instances": 34, "metric_value": 0.6723, "depth": 2}
		if obj[5]>0:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.2762, "depth": 3}
			if obj[9]<=19:
				return 'True'
			elif obj[9]>19:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=0:
					return 'False'
				elif obj[0]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]<=0:
			# {"feature": "Income", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[10]<=4:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[9]<=14:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[0]>2:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]>0:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[11]>0.0:
								return 'False'
							elif obj[11]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]<=2:
						return 'False'
					else: return 'False'
				elif obj[9]>14:
					return 'True'
				else: return 'True'
			elif obj[10]>4:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
