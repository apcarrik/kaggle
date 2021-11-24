def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[1]>0:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[9]<=2:
			# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.5226, "depth": 3}
			if obj[6]<=3.0:
				# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[7]<=2.0:
					return 'True'
				elif obj[7]>2.0:
					return 'False'
				else: return 'False'
			elif obj[6]>3.0:
				return 'False'
			else: return 'False'
		elif obj[9]>2:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
