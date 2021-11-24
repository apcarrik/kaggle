def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[4]>3:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[6]<=2.0:
				return 'False'
			elif obj[6]>2.0:
				# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[9]>1:
						return 'False'
					elif obj[9]<=1:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=3:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[2]<=3:
			return 'True'
		elif obj[2]>3:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]>0:
				return 'False'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
