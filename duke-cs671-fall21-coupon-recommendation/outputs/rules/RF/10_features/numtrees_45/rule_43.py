def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>0:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[4]<=20:
			# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[9]>1:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[9]<=1:
							return 'False'
						else: return 'False'
					elif obj[5]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[6]>2.0:
				return 'True'
			else: return 'True'
		elif obj[4]>20:
			return 'False'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
