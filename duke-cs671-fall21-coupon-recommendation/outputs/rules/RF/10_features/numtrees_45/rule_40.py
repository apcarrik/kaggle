def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.7025, "depth": 2}
		if obj[6]>1.0:
			return 'True'
		elif obj[6]<=1.0:
			# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=5:
					return 'False'
				elif obj[4]>5:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=1.0:
						return 'True'
					elif obj[5]>1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]>2:
		return 'False'
	else: return 'False'
