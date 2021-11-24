def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Time", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Coupon", "instances": 27, "metric_value": 0.9911, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[7]<=2:
				# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[11]<=2.0:
					return 'True'
				elif obj[11]>2.0:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8]>1:
						return 'False'
					elif obj[8]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>2:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[14]<=2:
					return 'False'
				elif obj[14]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[5]<=6:
				return 'False'
			elif obj[5]>6:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>1:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.7383, "depth": 2}
		if obj[8]>8:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[0]>1:
				# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[9]>0:
					return 'True'
				elif obj[9]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]<=1:
				# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[9]>0:
					return 'False'
				elif obj[9]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]<=8:
			return 'True'
		else: return 'True'
	else: return 'True'
