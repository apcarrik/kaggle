def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[6]<=7:
		# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[8]<=3.0:
			return 'True'
		elif obj[8]>3.0:
			return 'False'
		else: return 'False'
	elif obj[6]>7:
		# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[4]>1:
			# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>3:
					return 'False'
				elif obj[2]<=3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
