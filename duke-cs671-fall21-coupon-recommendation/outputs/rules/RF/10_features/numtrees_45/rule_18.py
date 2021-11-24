def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[4]>2:
			return 'False'
		else: return 'False'
	elif obj[1]>1:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[4]<=21:
			return 'True'
		elif obj[4]>21:
			return 'False'
		else: return 'False'
	else: return 'True'
