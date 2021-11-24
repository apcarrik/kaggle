def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[8]>1.0:
		# {"feature": "Education", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[5]<=2:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[6]>1:
				return 'True'
			elif obj[6]<=1:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[5]>2:
			# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[7]<=1.0:
					return 'True'
				elif obj[7]>1.0:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[8]<=1.0:
		return 'False'
	else: return 'False'
