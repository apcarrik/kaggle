def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[3]<=5:
				return 'True'
			elif obj[3]>5:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]>2.0:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
