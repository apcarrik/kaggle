def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[7]>1.0:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[2]>0:
			# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[4]<=3:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[5]>2:
					return 'False'
				elif obj[5]<=2:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0.0:
						return 'True'
					elif obj[6]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[7]<=1.0:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[5]>5:
			# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[3]>2:
				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[3]<=2:
				return 'False'
			else: return 'False'
		elif obj[5]<=5:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=3:
					return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
