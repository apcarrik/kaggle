def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[5]>4:
			# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[10]<=2:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>1:
						return 'False'
					elif obj[3]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]>2:
				return 'False'
			else: return 'False'
		elif obj[5]<=4:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
