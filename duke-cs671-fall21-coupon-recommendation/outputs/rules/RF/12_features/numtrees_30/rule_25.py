def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[4]>1:
		# {"feature": "Time", "instances": 22, "metric_value": 0.8454, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[5]>1:
					return 'False'
				elif obj[5]<=1:
					# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[4]<=1:
		# {"feature": "Bar", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[7]>-1.0:
			# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[5]>0:
				return 'True'
			elif obj[5]<=0:
				# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=0:
					return 'True'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=-1.0:
			return 'False'
		else: return 'False'
	else: return 'True'
