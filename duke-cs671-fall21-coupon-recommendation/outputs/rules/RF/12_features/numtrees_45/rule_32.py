def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[2]>1:
		# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 2}
		if obj[4]>0:
			return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[6]>2:
			# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[10]<=0:
				return 'False'
			elif obj[10]>0:
				return 'True'
			else: return 'True'
		elif obj[6]<=2:
			return 'True'
		else: return 'True'
	else: return 'False'
