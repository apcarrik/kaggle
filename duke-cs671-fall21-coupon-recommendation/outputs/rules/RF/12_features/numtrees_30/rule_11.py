def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.7219, "depth": 2}
		if obj[8]>1.0:
			# {"feature": "Age", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[4]>0:
				# {"feature": "Bar", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[7]<=1.0:
					return 'True'
				elif obj[7]>1.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=2:
						return 'False'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		elif obj[8]<=1.0:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[8]>0.0:
			return 'False'
		elif obj[8]<=0.0:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
