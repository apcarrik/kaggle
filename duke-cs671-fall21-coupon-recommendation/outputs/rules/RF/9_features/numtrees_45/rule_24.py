def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]<=6:
		# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[8]<=1:
			return 'True'
		elif obj[8]>1:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2]>1:
				return 'False'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>6:
		# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
