def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[5]>1:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9852, "depth": 2}
		if obj[6]<=8:
			# {"feature": "Time", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[1]>1:
				# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[4]>2:
					return 'False'
				elif obj[4]<=2:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=2:
						return 'True'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		elif obj[6]>8:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[1]>0:
					# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[8]>0.0:
						return 'True'
					elif obj[8]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[11]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Time", "instances": 23, "metric_value": 0.6666, "depth": 2}
		if obj[1]>1:
			return 'True'
		elif obj[1]<=1:
			# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[7]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
