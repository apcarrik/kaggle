def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[6]<=1.0:
		# {"feature": "Time", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[1]>0:
			# {"feature": "Passanger", "instances": 17, "metric_value": 0.5226, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[7]<=1.0:
				return 'True'
			elif obj[7]>1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]>1.0:
		# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[5]>1:
				return 'True'
			elif obj[5]<=1:
				return 'False'
			else: return 'False'
		elif obj[7]>2.0:
			return 'False'
		else: return 'False'
	else: return 'True'
