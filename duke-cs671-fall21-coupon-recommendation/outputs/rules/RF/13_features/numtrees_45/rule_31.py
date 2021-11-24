def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]<=5:
		# {"feature": "Education", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Occupation", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[7]<=7:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=0:
						return 'False'
					elif obj[3]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>7:
				return 'False'
			else: return 'False'
		elif obj[6]>2:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[7]>4:
				return 'True'
			elif obj[7]<=4:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]>5:
		return 'False'
	else: return 'False'
