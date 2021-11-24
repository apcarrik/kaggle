def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[7]<=14:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.65, "depth": 2}
		if obj[2]<=3:
			return 'True'
		elif obj[2]>3:
			# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[3]>0:
				# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[11]<=0:
					return 'True'
				elif obj[11]>0:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[7]>14:
		# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[4]>1:
			return 'False'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
