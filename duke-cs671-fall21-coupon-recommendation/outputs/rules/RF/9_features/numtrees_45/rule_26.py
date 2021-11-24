def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[8]<=2:
		# {"feature": "Education", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[3]>1:
			# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[1]>1:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[2]<=3:
					return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[5]<=2.0:
					return 'True'
				elif obj[5]>2.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	elif obj[8]>2:
		return 'False'
	else: return 'False'
