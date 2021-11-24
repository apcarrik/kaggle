def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[2]>1:
		# {"feature": "Bar", "instances": 28, "metric_value": 0.7496, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Time", "instances": 26, "metric_value": 0.6194, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Age", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[4]>1:
					# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[6]<=11:
						return 'True'
					elif obj[6]>11:
						# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[8]>1.0:
							return 'False'
						elif obj[8]<=1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]<=1:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>1:
						return 'False'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[7]>2.0:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
