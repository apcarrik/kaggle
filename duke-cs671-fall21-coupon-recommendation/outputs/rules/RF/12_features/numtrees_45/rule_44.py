def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[2]>1:
		# {"feature": "Gender", "instances": 17, "metric_value": 0.5226, "depth": 2}
		if obj[3]<=0:
			return 'True'
		elif obj[3]>0:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[5]>2:
				return 'True'
			elif obj[5]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[4]<=4:
			return 'False'
		elif obj[4]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
