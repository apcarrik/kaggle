def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[4]>0:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.5436, "depth": 2}
		if obj[6]>5:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			elif obj[7]>1.0:
				return 'True'
			else: return 'True'
		elif obj[6]<=5:
			return 'True'
		else: return 'True'
	elif obj[4]<=0:
		# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[6]>7:
				# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]>0.0:
						return 'False'
					elif obj[7]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[6]<=7:
				return 'False'
			else: return 'False'
		elif obj[8]>1.0:
			return 'True'
		else: return 'True'
	else: return 'False'
