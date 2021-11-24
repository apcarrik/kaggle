def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Gender", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]<=0:
		# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[6]>0:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[7]>4:
				# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[8]>4:
					return 'False'
				elif obj[8]<=4:
					return 'True'
				else: return 'True'
			elif obj[7]<=4:
				return 'True'
			else: return 'True'
		elif obj[6]<=0:
			return 'False'
		else: return 'False'
	elif obj[3]>0:
		# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[11]<=1.0:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[6]>1:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>1:
					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[6]<=1:
				return 'True'
			else: return 'True'
		elif obj[11]>1.0:
			return 'True'
		else: return 'True'
	else: return 'True'
