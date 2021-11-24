def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[7]>1:
		# {"feature": "Occupation", "instances": 50, "metric_value": 0.971, "depth": 2}
		if obj[8]<=16:
			# {"feature": "Bar", "instances": 44, "metric_value": 0.994, "depth": 3}
			if obj[10]<=2.0:
				# {"feature": "Gender", "instances": 38, "metric_value": 0.9678, "depth": 4}
				if obj[4]>0:
					# {"feature": "Income", "instances": 25, "metric_value": 0.9988, "depth": 5}
					if obj[9]>0:
						# {"feature": "Time", "instances": 22, "metric_value": 0.976, "depth": 6}
						if obj[1]>0:
							# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 7}
							if obj[2]>1:
								# {"feature": "Passanger", "instances": 14, "metric_value": 0.9852, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Age", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[5]>1:
										# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[6]>0:
											# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]>0.0:
													return 'True'
												elif obj[11]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[6]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=1:
										return 'False'
									else: return 'False'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							elif obj[2]<=1:
								# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[5]>1:
									return 'False'
								elif obj[5]<=1:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]>0:
										return 'True'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[9]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0:
					# {"feature": "Time", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[11]<=1.0:
								return 'False'
							elif obj[11]>1.0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]>2.0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]>16:
			return 'False'
		else: return 'False'
	elif obj[7]<=1:
		# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.8981, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Coupon", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[2]>1:
				# {"feature": "Time", "instances": 20, "metric_value": 0.8813, "depth": 4}
				if obj[1]>0:
					# {"feature": "Income", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[9]>2:
						return 'True'
					elif obj[9]<=2:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>2:
							return 'True'
						elif obj[0]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[5]<=3:
						return 'False'
					elif obj[5]>3:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[12]>1.0:
			return 'True'
		else: return 'True'
	else: return 'True'
