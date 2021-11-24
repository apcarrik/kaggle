def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Distance", "instances": 28, "metric_value": 0.8113, "depth": 2}
		if obj[14]<=2:
			# {"feature": "Coupon_validity", "instances": 24, "metric_value": 0.65, "depth": 3}
			if obj[3]>0:
				# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[10]>0.0:
					# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[5]<=3:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[12]<=2.0:
							return 'False'
						elif obj[12]>2.0:
							return 'True'
						else: return 'True'
					elif obj[5]>3:
						return 'True'
					else: return 'True'
				elif obj[10]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[14]>2:
			# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[4]<=0:
				return 'False'
			elif obj[4]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[7]>2:
		return 'False'
	else: return 'False'
