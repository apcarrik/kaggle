def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[6]>0.0:
		# {"feature": "Education", "instances": 43, "metric_value": 0.8841, "depth": 2}
		if obj[3]>0:
			# {"feature": "Passanger", "instances": 30, "metric_value": 0.971, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 24, "metric_value": 1.0, "depth": 4}
				if obj[4]<=9:
					# {"feature": "Time", "instances": 18, "metric_value": 0.9641, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[2]>0:
							# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[9]>1:
								# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									return 'False'
								else: return 'False'
							elif obj[9]<=1:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				elif obj[4]>9:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[3]<=0:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[6]<=0.0:
		# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
