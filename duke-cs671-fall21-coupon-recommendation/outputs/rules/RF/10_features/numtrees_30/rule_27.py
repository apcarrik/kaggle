def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[6]<=3.0:
		# {"feature": "Passanger", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[0]>0:
			# {"feature": "Bar", "instances": 24, "metric_value": 0.9544, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Coupon", "instances": 16, "metric_value": 1.0, "depth": 4}
				if obj[2]>2:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[1]>0:
								# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[4]>1:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]>1:
										return 'False'
									else: return 'False'
								elif obj[4]<=1:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							return 'False'
						else: return 'False'
					elif obj[7]>1.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			elif obj[5]>1.0:
				# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[6]>3.0:
		return 'False'
	else: return 'False'
