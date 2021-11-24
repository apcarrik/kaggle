def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1:
		# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Age", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=1.0:
						return 'True'
					elif obj[7]>1.0:
						return 'False'
					else: return 'False'
				elif obj[6]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[3]>3:
				return 'True'
			else: return 'True'
		elif obj[8]>1.0:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[0]>0:
			# {"feature": "Direction_same", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[9]<=0:
				return 'False'
			elif obj[9]>0:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
