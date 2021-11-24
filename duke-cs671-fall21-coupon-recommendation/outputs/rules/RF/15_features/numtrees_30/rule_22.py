def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[9]<=6:
		# {"feature": "Passanger", "instances": 28, "metric_value": 0.9852, "depth": 2}
		if obj[0]>1:
			# {"feature": "Gender", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[4]>0:
				return 'True'
			elif obj[4]<=0:
				# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[7]>0:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=3:
						return 'False'
					elif obj[5]>3:
						return 'True'
					else: return 'True'
				elif obj[7]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Children", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[8]>4:
					return 'False'
				elif obj[8]<=4:
					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[13]<=0:
						return 'True'
					elif obj[13]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[9]>6:
		return 'False'
	else: return 'False'
