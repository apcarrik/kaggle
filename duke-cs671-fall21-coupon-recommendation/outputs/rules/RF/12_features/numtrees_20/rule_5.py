def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Time", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 26, "metric_value": 0.8404, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.6098, "depth": 3}
			if obj[6]>1:
				# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.4855, "depth": 4}
				if obj[9]<=3.0:
					# {"feature": "Passanger", "instances": 18, "metric_value": 0.3095, "depth": 5}
					if obj[0]<=2:
						return 'True'
					elif obj[0]>2:
						# {"feature": "Gender", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]>1:
									return 'True'
								elif obj[5]<=1:
									return 'False'
								else: return 'False'
							elif obj[4]>2:
								return 'True'
							else: return 'True'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[9]>3.0:
					return 'False'
				else: return 'False'
			elif obj[6]<=1:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=3:
				return 'False'
			elif obj[4]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Education", "instances": 25, "metric_value": 0.9896, "depth": 2}
		if obj[5]>0:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Gender", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[3]>0:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[8]>1.0:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]>2:
								return 'True'
							elif obj[4]<=2:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]<=4:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=1:
												# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]<=1.0:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[6]<=6:
						return 'False'
					elif obj[6]>6:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>2.0:
				return 'True'
			else: return 'True'
		elif obj[5]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
