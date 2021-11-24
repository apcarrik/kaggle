def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[8]>1:
		# {"feature": "Bar", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[5]<=2.0:
			# {"feature": "Occupation", "instances": 25, "metric_value": 0.9988, "depth": 3}
			if obj[4]<=13:
				# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Coupon", "instances": 20, "metric_value": 0.9928, "depth": 5}
					if obj[2]>2:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[0]>1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]<=1:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]>1.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=2:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]>1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[4]>13:
				return 'True'
			else: return 'True'
		elif obj[5]>2.0:
			return 'False'
		else: return 'False'
	elif obj[8]<=1:
		# {"feature": "Coupon", "instances": 23, "metric_value": 0.6666, "depth": 2}
		if obj[2]>3:
			# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[3]>0:
				# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=17:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>1.0:
								return 'False'
							else: return 'False'
						elif obj[5]>0.0:
							return 'False'
						else: return 'False'
					elif obj[4]>17:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]<=3:
			return 'True'
		else: return 'True'
	else: return 'True'
