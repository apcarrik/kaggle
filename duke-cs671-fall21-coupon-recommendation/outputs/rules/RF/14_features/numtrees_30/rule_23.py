def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[7]<=7:
		# {"feature": "Distance", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[13]>1:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[11]<=2.0:
				return 'True'
			elif obj[11]>2.0:
				return 'False'
			else: return 'False'
		elif obj[13]<=1:
			# {"feature": "Income", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[8]<=7:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]>7:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[7]>7:
		# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[10]>1.0:
						return 'False'
					elif obj[10]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
