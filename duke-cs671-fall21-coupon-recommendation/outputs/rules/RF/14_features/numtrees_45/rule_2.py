def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[13]>1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[7]<=18:
			# {"feature": "Income", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[8]<=4:
				# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[4]<=4:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[9]>0.0:
						return 'False'
					elif obj[9]<=0.0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=1:
							return 'False'
						elif obj[2]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]>4:
					return 'True'
				else: return 'True'
			elif obj[8]>4:
				return 'False'
			else: return 'False'
		elif obj[7]>18:
			return 'True'
		else: return 'True'
	elif obj[13]<=1:
		# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[2]>0:
			return 'True'
		elif obj[2]<=0:
			# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]>1:
				return 'False'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
