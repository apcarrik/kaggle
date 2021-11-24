def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[6]<=10:
		# {"feature": "Distance", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[11]<=2:
			# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.5033, "depth": 3}
			if obj[9]<=1.0:
				return 'True'
			elif obj[9]>1.0:
				# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[10]<=0:
						return 'False'
					elif obj[10]>0:
						return 'True'
					else: return 'True'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[11]>2:
			return 'False'
		else: return 'False'
	elif obj[6]>10:
		# {"feature": "Time", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[2]>1:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
