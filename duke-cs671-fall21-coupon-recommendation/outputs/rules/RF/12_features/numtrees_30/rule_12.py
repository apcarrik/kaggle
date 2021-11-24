def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[4]<=4:
		# {"feature": "Passanger", "instances": 22, "metric_value": 0.9024, "depth": 2}
		if obj[0]>0:
			# {"feature": "Time", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[2]<=2:
					return 'False'
				elif obj[2]>2:
					# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]>1:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[10]<=0:
						return 'True'
					elif obj[10]>0:
						return 'False'
					else: return 'False'
				elif obj[8]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[4]>4:
		# {"feature": "Distance", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[11]<=2:
			return 'True'
		elif obj[11]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
