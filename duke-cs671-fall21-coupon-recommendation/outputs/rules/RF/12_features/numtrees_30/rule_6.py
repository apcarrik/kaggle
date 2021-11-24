def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 22, "metric_value": 0.7732, "depth": 2}
		if obj[6]>5:
			# {"feature": "Time", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[1]>0:
				# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[4]<=6:
					return 'True'
				elif obj[4]>6:
					# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[8]<=0.0:
						return 'False'
					elif obj[8]>0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[6]<=5:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[4]<=6:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[8]>0.0:
				return 'False'
			elif obj[8]<=0.0:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[5]<=0:
					return 'False'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>6:
			return 'True'
		else: return 'True'
	else: return 'False'
