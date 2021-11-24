def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[6]>4:
		# {"feature": "Distance", "instances": 14, "metric_value": 1.0, "depth": 2}
		if obj[11]<=1:
			# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[8]>0.0:
				return 'True'
			elif obj[8]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[11]>1:
			# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[4]<=6:
				return 'False'
			elif obj[4]>6:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]<=4:
		return 'True'
	else: return 'True'
